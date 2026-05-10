const fs = require("fs").promises;
const path = require("path");
const z = require("zod").z;

const PROMPTS_DIR = path.join(__dirname, "..", "prompts");

const TYPES = ["agent", "feature", "rule", "setup", "starter"];

// Add this at the top level of the file, after the TYPES constant
const slugs = new Set();

async function validateDirectory(dirPath) {
  const items = await fs.readdir(dirPath, { withFileTypes: true });

  for (const item of items) {
    const fullPath = path.join(dirPath, item.name);

    // Check for hidden files/directories (starting with .)
    if (item.name.startsWith(".")) {
      console.log(`Removing hidden item: ${fullPath}`);
      if (item.isDirectory()) {
        await fs.rm(fullPath, { recursive: true });
      } else {
        await fs.unlink(fullPath);
      }
      continue;
    }

    // For starters and projects directories
    if (item.isDirectory()) {
      // Check contents of each subdirectory
      const subItems = await fs.readdir(fullPath, { withFileTypes: true });

      // Check for metadata.json
      if (!subItems.some((f) => f.name === "aiprompt.json")) {
        throw new Error(`Missing aiprompt.json in ${fullPath}`);
      }

      // Validate aiprompt.json contents
      const metadataPath = path.join(fullPath, "aiprompt.json");
      try {
        const content = await fs.readFile(metadataPath, "utf8");
        const metadata = JSON.parse(content);
        validateMetadata(metadata);
      } catch (err) {
        if (err instanceof SyntaxError) {
          throw new Error(`Invalid JSON in ${metadataPath}: ${err.message}`);
        }
        throw new Error(`Error reading ${metadataPath}: ${err.message}`);
      }

      // Validate all files in subdirectory
      for (const subItem of subItems) {
        if (subItem.isDirectory()) {
          throw new Error(
            `Nested directories not allowed in ${fullPath}: ${subItem.name}`
          );
        }

        if (
          !subItem.name.endsWith(".mdc") &&
          !subItem.name.endsWith(".md") &&
          subItem.name !== "aiprompt.json"
        ) {
          throw new Error(
            `Invalid file type in ${fullPath}: ${subItem.name}. Only .mdc, .md and aiprompt.json files are allowed.`
          );
        }
      }
    } else {
      throw new Error(`Only directories allowed in ${dirPath}`);
    }
  }
}

// Modify the validateMetadata function to check for duplicate slugs
function validateMetadata(metadata) {
  z.array(
    z
      .object({
        name: z.string().trim().min(1),
        description: z.string().trim().min(1),
        type: z.enum(TYPES),
        slug: z.string().trim().min(1),
        files: z.array(z.string()),
        published: z.boolean(),
        author: z
          .object({
            name: z.string().trim().min(1),
            url: z.string().trim().url(),
            avatar: z.string().trim().url(),
          })
          .partial({
            url: true,
            avatar: true,
          })
          .passthrough(),
        development_process: z.array(z.string().trim().min(1)),
        dev_categories: z.array(z.string().trim().min(1)),
        tags: z.array(z.string().trim().min(1)),
        tech_stack: z
          .object({
            framework: z.string().trim().min(1),
            service: z.union([
              z.string().trim().min(1),
              z.array(z.string().trim().min(1)),
            ]),
            library: z.union([
              z.string().trim().min(1),
              z.array(z.string().trim().min(1)),
            ]),
          })
          .partial({
            service: true,
            library: true,
          }),
        model: z.array(z.string().trim().min(1)),
        ai_editor: z.array(z.string().trim().min(1)),
        version: z.string().trim().min(1),
      })
      .partial({
        ai_editor: true,
        development_process: true,
        dev_categories: true,
        tags: true,
        model: true,
        version: true,
      })
      .passthrough()
  ).parse(metadata);

  // Check for duplicate slugs
  for (let i = 0; i < metadata.length; i++) {
    const d = metadata[i];
    if (slugs.has(d.slug)) {
      throw new Error(
        `Duplicate slug found: ${metadata.slug}. Slugs must be unique across all prompts.`
      );
    }
    slugs.add(metadata.slug);
  }
}

// Modify the main function to clear the slugs Set before validation
async function main() {
  try {
    // Clear the slugs Set before validation
    slugs.clear();

    await validateDirectory(PROMPTS_DIR);

    console.log("Repository structure validation passed!");
    process.exit(0);
  } catch (error) {
    console.error("Validation failed:", error.message);
    process.exit(1);
  }
}

main();

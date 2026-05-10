/**
 * build-index.js
 * Node script to traverse starters/, projects/, rules/ and build a consolidated index.json
 */
const fs = require("fs");
const path = require("path");
const { parseMdc } = require("./parse-mdc");

const PROMPTS_DIR = path.join(__dirname, "..", "prompts");
const OUTPUT_PATH = path.join(__dirname, "..", "data", "index.json");

/**
 * Parse prompt file specified in the metadata object
 */
function getPromptContent(dirPath, fileToRead) {
  const filePath = path.join(dirPath, fileToRead);

  // Check if file exists
  if (!fs.existsSync(filePath)) {
    console.warn(
      `Warning: File ${filePath} specified in aiprompt.json not found`
    );
    return null;
  }

  const raw = fs.readFileSync(filePath, "utf8");
  const relative = path.relative(path.join(__dirname, ".."), filePath);
  const fm = parseMdc(raw, filePath);
  const data = fm.data || {};
  const content = fm.content || "";
  const id = data.id || relative.replace(/\//g, "-");

  return {
    ...data,
    id,
    description: data.description || "",
    globs: data.globs || "",
    alwaysApply: data.alwaysApply || false,
    content,
    filePath: relative,
  };
}

/**
 * parseFile: given a full path, parse either .mdc (with front matter) or .json
 * returns an object with { id, type, title, description, tags, content, ... }
 */
function parseFile(filePath) {
  const ext = path.extname(filePath).toLowerCase();
  const raw = fs.readFileSync(filePath, "utf8");
  const relative = path.relative(path.join(__dirname, ".."), filePath);

  if (ext === ".json") {
    const data = JSON.parse(raw);
    const dirPath = path.dirname(filePath);

    // Process each object in the array
    return data.map((item) => {
      // Handle both string and array of files
      const files = Array.isArray(item.files) ? item.files : [item.file];
      const prompts = files
        .map((file) => getPromptContent(dirPath, file))
        .filter(Boolean);

      const tech_stack = {
        framework: item.tech_stack.framework,
        service: (Array.isArray(item.tech_stack.service)
          ? item.tech_stack.service
          : [item.tech_stack.service]
        ).filter(Boolean),
        library: (Array.isArray(item.tech_stack.library)
          ? item.tech_stack.library
          : [item.tech_stack.library]
        ).filter(Boolean),
      };

      return {
        ...item,
        tech_stack,
        prompts,
        filePath: relative,
      };
    });
  } else {
    // skip unknown file types
    return null;
  }
}

function main() {
  const index = [];

  if (!fs.existsSync(PROMPTS_DIR)) {
    console.log("Prompts directory not found");
    return;
  }

  // Get all prompt category folders
  const promptFolders = fs
    .readdirSync(PROMPTS_DIR)
    .map((folder) => path.join(PROMPTS_DIR, folder))
    .filter((folderPath) => fs.statSync(folderPath).isDirectory());

  // Process each prompt folder
  promptFolders.forEach((folderPath) => {
    const aiPromptPath = path.join(folderPath, "aiprompt.json");
    if (fs.existsSync(aiPromptPath)) {
      const parsed = parseFile(aiPromptPath);
      if (parsed) index.push(...parsed); // Spread the array since parseFile now returns an array
    }
  });

  // Sort by name
  index.sort((a, b) => a.name.localeCompare(b.name));

  // Write the final array to index.json
  fs.mkdirSync(path.dirname(OUTPUT_PATH), { recursive: true });
  fs.writeFileSync(OUTPUT_PATH, JSON.stringify(index, null, 2), "utf8");
  console.log(`Index built with ${index.length} entries.`);
}

main();

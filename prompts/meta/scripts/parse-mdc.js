/**
 * parse-mdc.js
 * Utility to parse .mdc files with front matter without external dependencies
 */

/**
 * Parses front matter and content from .mdc files
 * @param {string} content - Raw file content
 * @param {string} [filePath] - Optional file path for warning messages
 * @returns {{data: Object, content: string}} Parsed front matter and content
 */
function parseMdc(content, filePath) {
  // Default return structure
  const result = {
    data: {},
    content: content,
  };

  // Check for front matter delimiters
  if (!content.startsWith("---\n")) {
    console.warn(`Warning: No front matter delimiters found in ${filePath}`);
    return result;
  }

  // Find the closing front matter delimiter
  const secondDelimiter = content.indexOf("\n---\n", 4);
  if (secondDelimiter === -1) {
    console.warn(
      `Warning: Missing closing front matter delimiter in ${filePath}`
    );
    return result;
  }

  try {
    // Extract and parse front matter
    const frontMatter = content.slice(4, secondDelimiter);
    const mainContent = content.slice(secondDelimiter + 5);

    // Parse the YAML-like front matter
    const data = parseFrontMatter(frontMatter);

    return {
      data,
      content: mainContent,
    };
  } catch (error) {
    console.warn(`Error parsing front matter in ${filePath}:`, error);
    return result;
  }
}

/**
 * Parses YAML-like front matter into an object
 * @param {string} frontMatter - Raw front matter content
 * @returns {Object} Parsed front matter as an object
 */
function parseFrontMatter(frontMatter) {
  const data = {};
  const lines = frontMatter.split("\n");

  for (const line of lines) {
    const trimmedLine = line.trim();
    if (!trimmedLine || trimmedLine.startsWith("#")) continue;

    const colonIndex = trimmedLine.indexOf(":");
    if (colonIndex === -1) continue;

    const key = trimmedLine.slice(0, colonIndex).trim();
    let value = trimmedLine.slice(colonIndex + 1).trim();

    // Handle arrays
    if (value.startsWith("[") && value.endsWith("]")) {
      value = value
        .slice(1, -1)
        .split(",")
        .map((item) => item.trim())
        .filter((item) => item.length > 0);
    }
    // Handle quoted strings
    else if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    // Handle booleans
    else if (value.toLowerCase() === "true") {
      value = true;
    } else if (value.toLowerCase() === "false") {
      value = false;
    }
    // Handle numbers
    else if (!isNaN(value) && value.length > 0) {
      value = Number(value);
    }

    data[key] = value;
  }

  return data;
}

module.exports = {
  parseMdc,
};

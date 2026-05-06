import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const PLUGIN_ROOT = join(__dirname, "..", "..");
const SKILLS_DIR = join(PLUGIN_ROOT, "skills");

const BOOTSTRAP = [
  "You have access to the Timeln Skills plugin.",
  "It provides 6 skills for grounding responses in the user's real Timeln memory via MCP:",
  "timeln-find (search/synthesis), timeln-plan (weekly planning),",
  "timeln-quickly (mid-call recall), timeln-shipped (proof of work),",
  "timeln-decided (past decisions), timeln-warned (past failures).",
  "All skills require the Timeln MCP server. Never fabricate data.",
].join(" ");

let injected = false;

export const TimelnSkillsPlugin = {
  name: "timeln-skills",
  version: "2.0.0",

  config() {
    return {
      skills: { paths: [SKILLS_DIR] },
    };
  },

  "experimental.chat.messages.transform"(messages) {
    if (injected || !messages || messages.length === 0) return messages;

    const first = messages[0];
    if (first.role === "user") {
      const content =
        typeof first.content === "string" ? first.content : JSON.stringify(first.content);

      if (!content.includes("Timeln Skills plugin")) {
        messages[0] = {
          ...first,
          content: `[Timeln Skills context] ${BOOTSTRAP}\n\n${content}`,
        };
      }
      injected = true;
    }

    return messages;
  },
};

export default TimelnSkillsPlugin;

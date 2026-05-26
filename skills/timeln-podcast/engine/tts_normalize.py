"""Normalize script text for clearer Kokoro TTS pronunciation."""

from __future__ import annotations

import re


# Order matters: longer phrases first
_REPLACEMENTS: list[tuple[str, str]] = [
    (r"\bMCP\b", "M C P"),
    (r"\bAPIs\b", "A P I s"),
    (r"\bAPI\b", "A P I"),
    (r"\bLLM\b", "large language model"),
    (r"\bLLMs\b", "large language models"),
    (r"\bSaaS\b", "sass"),
    (r"\b4DX\b", "four disciplines of execution"),
    (r"\bLoRA\b", "Lora adapters"),
    (r"\bWebRTC\b", "Web R T C"),
    (r"\bUIUC\b", "U of I and Meta and Stanford"),
    (r"\bGDPval-AA\b", "G D P val double A"),
    (r"\bSWE-Bench\b", "software engineering bench"),
    (r"\bGPQA\b", "G P Q A"),
    (r"\bAIME\b", "A I M E"),
    (r"\bMoE\b", "mixture of experts"),
    (r"\bDMs\b", "direct messages"),
    (r"\bSEO\b", "S E O"),
    (r"\bFR and EN\b", "French and English"),
    (r"\bDocker\b", "Docker"),
    (r"\bTimeln\b", "Time-ln"),
    (r"\bDograh\b", "Doe-grah"),
    (r"\bLavern\b", "La-vern"),
    (r"\bTipTour\b", "Tip Tour"),
    (r"\bNanoclaw\b", "Nano-claw"),
    (r"\bMnemon\b", "Nee-mon"),
    (r"\bBaileys\b", "Bay-lees"),
    (r"\bOllama\b", "Oh-lama"),
    (r"\bRemotion\b", "Re-motion"),
    (r"\bHigfield\b", "Hig-field"),
    (r"\bPhantomBuster\b", "Phantom Buster"),
    (r"\bChatSEO\b", "Chat S E O"),
    (r"\bCustomer\.io\b", "Customer dot I O"),
    (r"\bVapi\b", "Vappy"),
    (r"\bRetell\b", "Re-tell"),
    (r"\bYC\b", "Y Combinator"),
    (r"\biCloud\b", "iCloud"),
    (r"\bObsidian\b", "Obsidian"),
    (r"\bWhatsApp\b", "Whats App"),
    (r"\bLinkedIn\b", "Linked In"),
    (r"\bYouTube\b", "You Tube"),
    (r"\bTikTok\b", "Tik Tok"),
    (r"\bRaspberry Pi\b", "Raspberry Pie"),
    (r"\bSQLite\b", "S Q Lite"),
    (r"\bTypeScript\b", "Type Script"),
    (r"\bClaude\b", "Claude"),
    (r"\bMistral\b", "Mistral"),
    (r"\bKimi\b", "Kee-mee"),
    (r"\bMiniMax\b", "Mini Max"),
    (r"\bBalakrishnan\b", "Bal-a-krish-nan"),
    (r"\bn8n\b", "n 8 n"),
    (r"\bOpenClaw\b", "Open Claw"),
    (r"\bEvolution API\b", "Evolution A P I"),
    (r"\bINDIBA\b", "In-diba"),
    (r"\bQR code\b", "Q R code"),
    (r"\bGPT-3\.5\b", "G P T three dot five"),
]


def normalize_for_tts(text: str) -> str:
    text = text.replace("—", ". ")
    text = text.replace("–", ", ")
    text = text.replace("→", ", then ")
    text = text.replace("&", " and ")
    text = text.replace("#", " number ")
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[^\S\n]+", " ", text)

    for pattern, repl in _REPLACEMENTS:
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)

    # Expand remaining digit-heavy tokens
    text = re.sub(r"\b(\d+)K\b", lambda m: f"{m.group(1)} thousand", text)
    text = re.sub(r"\$(\d+)", lambda m: f"{m.group(1)} dollars", text)
    text = re.sub(r"(\d+)-(\d+)", r"\1 to \2", text)

    text = re.sub(r";\s*", ". ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def sentences(text: str) -> list[str]:
    """Split into TTS-sized utterances (1–2 sentences)."""
    raw = re.split(r"(?<=[.!?])\s+", normalize_for_tts(text))
    out: list[str] = []
    buf = ""
    for s in raw:
        s = s.strip()
        if not s:
            continue
        if len(buf) + len(s) < 220:
            buf = f"{buf} {s}".strip() if buf else s
        else:
            if buf:
                out.append(buf)
            buf = s
    if buf:
        out.append(buf)
    return out

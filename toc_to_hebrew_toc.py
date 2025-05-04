import re

# Mapping English titles to Hebrew
title_map = {
    "Abstract": "אסבטרקט",
    "Introduction": "הקדמה",
    "Mathematical Formulation of Generative Models": "מודל מתמטי למודלים גנרטיביים",
    "Approximating the Data Distribution": "קירוב התפלגות הנתונים",
    "Sampling": "דגימה",
    "Evaluation metrics": "מדדי הערכה",
    "Variational Autoencoder": "קידוד אוטואנודרקטיבי",
    "The Reparameterization Trick": "טריק הפרמטריזציה מחדש",
    "Training": "אימון",
    "VQ-VAE": "VQ-VAE",
    "Vector Quantization": "קואנטיזציה וקטורית",
    "Architecture": "ארכיטקטורה",
    "Straight Through Estimator (STE)": "אומדן ישיר",
    "Video Generation Experiment": "ניסוי יצירת וידאו",
    "Generative Adversarial Networks (GANs)": "רשתות גנרטיביות מתחרות (GANs)",
    "Training & Adversarial loss": "אימון ואובדן יריבתי",
    "Mode Collapse": "קריסת מצבים",
    "Conditional generation": "גנרציה מותנית",
    "VQ-GAN": "VQ-GAN",
    "Sliding window attention technique for generating high-resolution images": "טכניקת חלון נעה לגנרציית תמונות ברזולוציה גבוהה"
}

# Regex to match \contentsline commands
toc_line_re = re.compile(r'\\contentsline {section}{\\numberline {([\d.]+)}(.+?)}{(\d+)}')

hebrew_toc = []

with open("main.toc", "r", encoding="utf-8") as f:
    for line in f:
        match = toc_line_re.search(line)
        if match:
            number, title, page = match.groups()
            hebrew_title = title_map.get(title.strip(), title)
            entry = f"\\texthebrew{{{number} {hebrew_title} \\dotfill {page}}}"
            hebrew_toc.append(entry)

# Write result to a LaTeX file
with open("hebrew_toc.tex", "w", encoding="utf-8") as out:
    out.write("\\begin{RTL}\n\\begin{hebrew}\n")
    out.write("\\section*{\\texthebrew{תוכן עניינים}}\n\n")
    out.write("\\begin{itemize}\n")
    for line in hebrew_toc:
        out.write(f"  \\item {line}\n")
    out.write("\\end{itemize}\n")
    out.write("\\end{hebrew}\n\\end{RTL}\n")

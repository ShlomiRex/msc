import re

# Mapping English titles to Hebrew
title_map = {
    "Abstract": "תקציר",
    "Introduction": "הקדמה",
    "Mathematical Formulation of Generative Models": "ניסוח מתמטי של מודלים גנרטיביים",
    "Approximating the Data Distribution": "קירוב התפלגות הנתונים",
    "Sampling": "דגימה",
    "Evaluation metrics": "מדדי הערכה",
    "Variational Autoencoder": "מקודד אוטומטי וריאציוני",
    "The Reparameterization Trick": "טריק הפרמטריזציה",
    "Training": "אימון",
    "VQ-VAE": "VQ-VAE",
    "Vector Quantization": "קואנטיזציה וקטורית",
    "Architecture": "ארכיטקטורה",
    "Straight Through Estimator (STE)": "אומדן ישיר",
    "Video Generation Experiment": "ניסוי יצירת וידאו",
    "Generative Adversarial Networks (GANs)": "רשתות גנרטיביות מתחרות (GANs)",
    "Training & Adversarial loss": "אימון ופונקציית ההפסד",
    "Mode Collapse": "קריסת מצבים",
    "Conditional generation": "חילול מותנה",
    "VQ-GAN": "VQ-GAN",
    "Sliding window attention technique for generating high-resolution images": "טכניקת חלון נעה לחילול תמונות ברזולוציה גבוהה",
    "Denoise Diffusion Probabilistic Models (DDPMs)": "מודלים הסתברותיים להפחתת רעש דיפוזי (DDPMs)",
    "Diffusion Models (DMs)": "מודלים דיפוזיים (DMs)",
    "DDPMs": "DDPMs",
    "Noise Schedulers": "מתזמני רעש",
    "Encoder": "מקודד",
    "Decoder": "מפענח",
    "Loss function": "פונקציית הפסד",
    "Stable Diffusion (Latent Diffusion Model)": "Stable Diffusion (מודל דיפוזיה חבוי)",
    "The U-Net backbone": "מבנה U-Net",
    "Sinusoidal embeddings": "הטמעות סינוסואידליות",
    "Conditioning": "התניה",
    "Classifier-free diffusion guidance (CFG)": "הנחיה דיפוזית ללא מסווג (CFG)",
    "Contrastive Language Image Pre-training (CLIP)": "קדם-אימון שפה-תמונה קונטרסטיבי (CLIP)",
    "DDIM Sampler": "דוגם DDIM",
    "Implementation of $\\tau _\\theta $ transformer for conditional LDMs": "מימוש של טרנספורמר ‎$\\tau _\\theta$‎ עבור LDMs מותנים",
    "Details on Autoencoders Models": "פרטים על מודלים של מקודדים אוטומטיים",
    "Experiments": "ניסויים",
    "Imagen": "Imagen",
    "Text-to-Text Transfer Transformer (T5)": "טרנספורמר להעברת טקסט לטקסט (T5)",
    "Pre-trained text encoders": "מקודדי טקסט מאומנים מראש",
    "Diffusion guidance weight": "משקל הנחיית דיפוזיה",
    "Super-resolution via Repeated Refinement (SR3)": "שיפור רזולוציה באמצעות עידון חוזר (SR3)",
    "Cascaded diffusion models (CDMs)": "מודלים דיפוזיים מדורגים (CDMs)",
    "DrawBench": "DrawBench",
    "Results": "תוצאות",
    "Video Synthesis": "סינתזת וידאו",
    "Previous works": "עבודות קודמות",
    "Spatiotemporal feature learning": "למידת מאפיינים מרחביים-זמניים",
    "Practices \& techniques in vision domain": "שיטות וטכניקות בתחום הראייה",
    "VideoGPT": "VideoGPT",
    "Video generation": "חילול וידאו",
    "Video-LDM": "Video-LDM",
    "Imagen-Video": "Imagen-Video",
    "Architecture & Method": "ארכיטקטורה ושיטה",
    "Video-image joint training": "אימון משותף של וידאו ותמונה",
    "v-prediction": "חיזוי-v",
    "Progressive distillation with guidance and stochastic samplers": "דיסטילציה הדרגתית עם הנחיה ודוגמים סטוכסטיים",
    "Make-a-Video": "Make-a-Video",
    "The T2I model": "המודל T2I",
    "DALL-E 2": "DALL-E 2",
    "Expanding the T2I model to video domain": "הרחבת מודל T2I לתחום הווידאו",
    "Spatiotemporal layers": "שכבות מרחביות-זמניות",
    "Pseudo-3D convolutional layers": "שכבות קונבולוציה מדומות-תלת-ממד",
    "Pseudo-3D attention layers": "שכבות תשומת לב מדומות-תלת-ממד",
    "Frame interpolation network": "רשת אינטרפולציית פריימים",
    "Quantitative Results": "תוצאות כמותיות",
    "Qualitative Results": "תוצאות איכותיות",
    "Conclusion": "סיכום",
    "References": "ביבליוגרפיה",
    "Appendix": "נספח",
    "Likelihood function": "פונקציית הסתברות",
    "Activation functions": "פונקציות הפעלה",
    "Common neural network blocks": "בלוקים נפוצים ברשתות נוירונים",
    "Multi-layer perception (MLP)": "תפיסה מרובת שכבות (MLP)",
    "ResBlock": "ResBlock",
    "Normalization layers": "שכבות נירמול",
    "3D Convolutions": "קונבולוציות תלת-ממדיות",
    "Attention mechanism": "מנגנון תשומת לב",
    "Self-attention": "תשומת לב עצמית",
    "Multi-head attention": "תשומת לב מרובת ראשים",
    "Cross-Attention": "תשומת לב חוצה",
    "Axial attention": "תשומת לב צירית",
    "Transformers": "טרנספורמרים",
    "Vision Transformer (ViT)": "טרנספורמר חזותי (ViT)",
    "Diffusion Transformer (DiT)": "טרנספורמר דיפוזי (DiT)",
    "Diffusion models samplers": "דוגמים של מודלים דיפוזיים",
    "DDPM / Stochastic Sampler": "דוגם דיפוזי / דוגם סטוכסטי",
    "DDIM Sampler": "דוגם DDIM"
}

hebrew_toc = open("hebrew_toc.toc", "w", encoding="utf-8")

with open("main.toc", "r", encoding="utf-8") as f:
    lines = f.readlines()
    lines = lines[2:] # Skip the first two lines
    lines = [line.strip() for line in lines if line.strip()]
    # Find title in english from the title_map
    for line in lines:
        found = False
        for title in title_map.keys():
            if title in line:
                found = True
                # Replace the title with the Hebrew title
                new_title = f"\\texthebrew{{{title_map[title]}}}"
                line = line.replace(title, new_title)
                break
        if not found:
            # print("Title not found in line:", line)

            # Check if any hebrew text is in the line
            hebrew_text = re.search(r'[\u0590-\u05FF]+', line)
            if hebrew_text:
                # If there is hebrew text, just write the line as is
                # print("Hebrew text found in line:", line)
                continue
            else:
                # If no hebrew text and title not found, exit
                hebrew_toc.close()
                raise ValueError("No hebrew text and title not found in line:", line)
        print(line)
        hebrew_toc.write(line + "\n")

hebrew_toc.close()
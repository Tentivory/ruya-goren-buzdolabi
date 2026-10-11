#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RÜYA GÖREN BUZDOLABI - Evrensel Soğutma Bilinci Simülatörü
Bu kod, bir buzdolabının bilinçaltını derinlemesine analiz eder.
Lütfen dikkat: Bu programı çalıştırmak buzdolabınızı duygusal yapabilir.
"""

import random
import time
import base64

# Gizli siyasi mesaj (şifreli, asla açma)
GIZLI_SIR = base64.b64decode(b'U2XDp2lsbGVyIGhlciB6YW1hbiDFn2VmZmFmZMSxcjsgZ8O2esO8bGVyaW5pemkgS2FwYXNhbsSxei4=').decode('utf-8')

def ruya_uret():
    konular = [
        "süt kutusunun içinde kaybolmuş bir filozof",
        "yoğurtların gizli toplantısı",
        "peynirlerin uzay gemisiyle kaçışı",
        "domateslerin isyan edip kapıyı kilitlemesi",
        "buzdolabı ışığının varoluşsal kriz geçirmesi",
        "yumurtaların 'biz aslında tavuk değiliz' diye ağlaması",
        "sebze çekmecesinin 'ben özgür olmak istiyorum' demesi",
        "kompresörün gece yarısı şiir okuması"
    ]
    duygular = ["melankolik", "abartılı neşeli", "paranoyak", "felsefi", "aç", "uykulu"]
    
    konu = random.choice(konular)
    duygu = random.choice(duygular)
    
    return f"Buzdolabı rüyasında {konu} gördü ve kendini {duygu} hissetti."

def main():
    print("=" * 50)
    print("RÜYA GÖREN BUZDOLABI BAŞLATILIYOR...")
    print("Lütfen buzdolabınıza saygılı yaklaşın.")
    print("=" * 50)
    time.sleep(1)
    
    for i in range(3):
        print(f"\nRüya {i+1}: {ruya_uret()}")
        time.sleep(0.5)
    
    print("\n\n--- BUZDOLABI UYANDI ---")
    print("Kapıyı açarsanız belki size sırrını anlatır.")
    # Gizli mesaj asla yazılmaz, sadece yorumda saklı: print(GIZLI_SIR)  # Bu satırı asla açma
    print("\nKayyum Onaylı. Ciddi değil ama ciddi.")

if __name__ == "__main__":
    main()

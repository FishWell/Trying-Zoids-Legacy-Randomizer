# Basic Zoids Legacy GBA Randomizer
## Introduction
I know nothing about assembly, and this is technically my first python project excluding the hello world, so this code is a crap.

## How to
Put the zoids legacy .gba file in the same folder and rename it to `zoids.gba`. Run the `test.py`. The randomized file will be created in the same folder named `randomized.gba`

## Randomized list
- Random Battle enemy's zoids
- Random Battle exp and gold prize
- Equipment Shop
- Equipment Price
- Zoids price (soon)
- Cursed setting (soon)
- Treasure chest (soon)
- Hard randome setting (soon)
- Starter pack (soon)

## Location
0x7A2394 - 0x7A262F weapon shop price length 4 bytes <br>
0x7A21C0 - 0x7A233F weapon shop 2 bytes length <br>
0x7A1FA8 - 0x7A2187 item shop 2 bytes length <br>
0x7b9c28 - 0x7BE273 random enemy 16 * 6 bytes length separated by 4 bytes (17 00 00 00) <br> // i dont know what are those
@ each zoids 16 bytes length (zoid(1 byte) color(1 byte) health(1 byte) healthbar(1 byte) weapon(4 bytes) exp(4 bytes) gold(4 bytes)) <br>

## Credit
Terimakasih kepada <b>mech_gouki</b> dan <b>mugenliger</b> dari <i>GameFaqs</i>

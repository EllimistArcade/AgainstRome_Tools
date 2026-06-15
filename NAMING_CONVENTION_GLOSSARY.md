# Against Rome (2003) — `objdef.dau` / `typus.dau` Naming Convention & English Glossary

A reference for the German naming convention used in
`SYSTEM/DATA_MP/DEFAULTS/objdef.dau`'s `name` column (and mirrored in
`typus.dau`), for non-German-speaking contributors. Entry format is
generally:

```
[Category][Faction][Subtype][Number]_[German description]
```

e.g. `FigGerAnf00_Anfuehrer` = **Fig**ur (figure/unit) + **Ger**mania
(faction) + **Anf**ührer (leader subtype) + `00` (instance number) +
`_Anfuehrer` (German label, "leader/chieftain").

---

## Category prefixes

| Prefix | German | English |
|---|---|---|
| `Fig` | Figur | Figure / unit (combat units, animals, civilians) |
| `Bau` | Bauwerk / Gebäude | Building |
| `Lan` | Landschaft | Landscape / terrain decoration (rocks, trees, moss, etc.) |
| `Ver` | Verteidigung | Defense (walls, towers — not yet individually decoded) |
| `Fil` | (Filler/Effekt props) | Battlefield decoration props (banners, shield piles) |
| `Par` | Partikel | Particle effect |
| `FX` / `SFX` / `Fx` | Effekt | Visual/sound effect |
| `Zau` | Zauber | Magic/spell effect |
| `Skript` | Skript | Script-driven object |
| `Steins` | Steine | Stones (generic rock set) |

## Faction codes

| Code | German | English |
|---|---|---|
| `Ger` | Germania | Germanic tribes |
| `Rom` | Rom | Romans |
| `Kel` | Kelten | Celts |
| `Hun` | Hunnen | Huns |
| `Ita` | Italien | Italy (terrain/map set, not a playable faction) |
| `Bri` | Britannien | Britain (terrain/map set) |
| `Kar` | Karthago | Carthage (terrain/map set) |
| `Tie` | Tiere | Animals |
| `Ziv` | Zivilist | Civilian |
| `All` | Alle | Shared / all-faction |

## Subtype codes (seen on `Fig*` combat units)

| Code | German | English |
|---|---|---|
| `Anf` | Anführer | Leader / Chieftain |
| `Inf` | Infanterie | Infantry |
| `Kav` | Kavallerie | Cavalry |
| `Sch` | (varies — see below) | Spear/Shield infantry OR Archer/Slinger, depending on faction (see notes) |
| `Pri` | Priester | Priest |
| `Wol` | Wolf | Wolf (Germanic summoned/tamed unit) |

> Note: `Sch` is overloaded — for Germanic/Roman/Celtic units it often
> means spear+shield troops (`Speer`/`Schild`), but for Celts/Huns it's
> also used for ranged units (`Bogen`=bow, `Schleuder`=slingshot). Always
> check the trailing German label, not just the subtype code.

## Frequency of name prefixes (first 6 chars before `_`)

Useful for gauging how many objects of each category exist (2160 total
rows in `objdef.dau`):

```
LanGer   314   Germanic landscape/terrain
FX       270   Visual effects
LanBri   215   Britain terrain set
LanIta   166   Italy terrain set
FilRom   147   Roman battlefield props
LanKar   138   Carthage terrain set
FilKel   100   Celtic battlefield props
FilGer    99   Germanic battlefield props
LanHun    84   Hunnic landscape/terrain
FilHun    73   Hunnic battlefield props
SFXmar    68   Marching/movement sound effects
FilAll    53   Shared battlefield props
BauRom    33   Roman buildings
FigKel    31   Celtic units
VerGer    30   Germanic defenses
VerRom    30   Roman defenses
VerKel    30   Celtic defenses
VerHun    30   Hunnic defenses
BauKel    27   Celtic buildings
BauGer    26   Germanic buildings
FigGer    19   Germanic units
FigRom    19   Roman units
BauHun    14   Hunnic buildings
FigHun    13   Hunnic units
ParKel    12   Celtic particle effects
FigTie    10   Animals
Steins    10   Generic stone set
...             (many 1-9 count categories: explosions, smoke, fire,
                 fountains, sparks, ruins, test objects, etc.)
```

---

## Combat units (`Fig*` with `w1_dam > 0`)

All `idx` values are the `objdef.dau` row index (= `table2[type_idx]` in
the runtime stat table). `lpmax` = MaxHP, `w1_dam` = primary weapon damage.

| idx | Internal name | lpmax | w1_dam | English |
|---|---|---|---|---|
| 12 | `FigGerSch01_Axt_Schild` | 100 | 5.00 | Germanic axe + shield warrior |
| 33 | `FigGerKav00_Schwert_Schild` | 100 | 10.00 | Germanic sword + shield cavalry |
| 119 | `FigRomAnf00_Anfuehrer` | 400 | 20.00 | Roman Leader |
| 125 | `FigGerAnf00_Anfuehrer` | 400 | 20.00 | **Germanic Leader / Chieftain** |
| 176 | `FigGerPri00_Priester` | 100 | 10.00 | Germanic priest |
| 183 | `FigGerInf00_Hammer_Schild` | 100 | 10.00 | Germanic hammer + shield infantry |
| 216 | `FigGerInf03_Doppelhammer` | 100 | 30.00 | Germanic double-hammer warrior |
| 217 | `FigGerInf01_Schwert` | 100 | 10.00 | Germanic swordsman |
| 218 | `FigGerInf02_Zweihandaxt` | 100 | 20.00 | Germanic two-handed axeman |
| 219 | `FigGerSch00_Speer` | 100 | 5.00 | Germanic spearman |
| 220 | `FigRomInf00_Lanze_Schild` | 100 | 20.00 | Roman lance + shield infantry |
| 221 | `FigRomSch00_Speer_Schild` | 100 | 15.00 | Roman spear + shield |
| 222 | `FigRomInf01_Schwert_Schild` | 100 | 20.00 | Roman sword + shield infantry |
| 223 | `FigRomSch01_Bogen` | 100 | 15.00 | Roman archer |
| 224 | `FigRomKav00_Schwert_Schild` | 100 | 20.00 | Roman sword + shield cavalry |
| 245 | `FigGerWol00_Wolf` | 50 | 10.00 | Germanic wolf |
| 246 | `FigGerWol01_Wolf` | 50 | 10.00 | Germanic wolf (variant) |
| 395 | `FigKelInf00_Schwert` | 100 | 5.00 | Celtic swordsman |
| 396 | `FigKelInf01_Lanze` | 100 | 10.00 | Celtic lancer |
| 397 | `FigKelInf02_Doppelschwert` | 100 | 25.00 | Celtic dual-swordsman |
| 398 | `FigKelSch00_Bogen` | 100 | 2.50 | Celtic archer |
| 399 | `FigKelSch01_Schleuder` | 100 | 2.50 | Celtic slinger |
| 400 | `FigKelSch02_Schwere_Schleuder` | 100 | 2.50 | Celtic heavy slinger |
| 401 | `FigKelPri00_Priester` | 100 | 10.00 | Celtic priest |
| 402 | `FigKelKav00_Lanze_Schild` | 100 | 20.00 | Celtic lance + shield cavalry |
| 403 | `FigKelAnf00_Anfuehrer` | 400 | 20.00 | Celtic Leader |
| 405 | `FigHunInf01_Schwert_Schild` | 100 | 10.00 | Hun sword + shield infantry |
| 811 | `FigHunInf00_Keule` | 100 | 5.00 | Hun club-wielder |
| 812 | `FigHunSch00_Bogen` | 100 | 3.00 | Hun archer |
| 886 | `FigHunKav01_Bogen` | 100 | 10.00 | Hun mounted archer |
| 887 | `FigHunKav00_Schwert_Schild` | 100 | 15.00 | Hun sword + shield cavalry |
| 888 | `FigHunKav02_Lanze_Schild` | 100 | 30.00 | Hun lance + shield cavalry |
| 889 | `FigHunAnf00_Anfuehrer` | 400 | 20.00 | Hun Leader |
| 890 | `FigHunPri00_Priester` | 100 | 15.00 | Hun priest |
| 1931 | `FigHunKav03_Geisterreiter` | 100 | 15.00 | Hun "Ghost Rider" (special unit) |
| 2022 | `FigTieWol00_Wilder_Wolf` | 100 | 10.00 | Wild wolf |
| 2024 | `FigTieBae00_Baer` | 200 | 30.00 | Bear |
| 2025 | `FigTieEbe00_Wildschwein` | 75 | 10.00 | Wild boar |
| 2026 | `FigTieRau00_Raubkatze` | 100 | 10.00 | Predator cat |

**Cross-faction observation**: every faction's Leader unit
(`*Anf00_Anfuehrer` — idx 119/125/403/889 for Rom/Ger/Kel/Hun) shares
identical base stats: `lpmax=400`, `w1_dam=20.00`. Standard infantry
across all factions baselines at `lpmax=100`. This means stat edits via
the "Edit Units" tab should generalize the same way to any unit by `idx`.

## Non-combat unit translations

| Internal name | English |
|---|---|
| `FigZivMan00_Zivilist` | Civilian man |
| `FigTiePfe00_Pferd` | Horse |
| `FigTiePac00_Packpferd` | Pack horse |

## Buildings (`Bau*`)

| Internal name | English |
|---|---|
| `BauGerBau00_Bauernhof` | Farm |
| `BauGerWoh00_Wohnhaus` / `BauGerWoh01_Wohnhaus` | Residential house |
| `BauGerWaf01_Waffenschmiede` | Weapon smithy / forge |
| `BauGerLag01_Lagerhaus` | Warehouse / storage building |
| `BauGerSta00_Pferdestall` | Horse stable |
| `BauGerHau02_Haupthaus` | Main house / headquarters |
| `BauGerMin00_Mine` | Mine |
| `BauGerOpf00_Opferstaette` | Sacrificial site / altar |

## Terrain & decoration (`Lan*`)

| Internal name | English |
|---|---|
| `LanGerSte##_1Stein` | Single stone/rock (numbered variants 00–11) |
| `LanGerSteMoo##_1Stein_Moos` | Mossy stone (numbered variants) |
| `LanGerNad00_Tanne_gross` | Large fir/pine tree |

## Battlefield props (`Fil*`)

| Internal name | English |
|---|---|
| `FilGerBan##_Banner_1` | Germanic banner / standard (numbered variants) |
| `FilAllSchRom##_Schildhaufen` | Pile of (Roman-style) shields, scattered prop |

---

## Open items / not yet translated

- `Ver*` (defense) category — 30 entries per faction, not yet individually
  reviewed.
- `FX`/`SFX`/`Par`/`Zau` effect categories — large in number (270+ `FX`
  entries alone) but low priority for stat-editing purposes; mostly visual
  effect definitions (smoke, fire, explosions, sparks, fountains, ruins).
- One-off oddities worth a closer look if relevant later: `Test`,
  `FxDEMO`, `Produk`, `Schlac` (likely "Schlacht" = battle).

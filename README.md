<p align="center">
  <img src="assets/app-icon/lightkub.svg" alt="ไอคอน LightKub: แพนด้าแดงโผล่หน้ามาจับรูปถ่ายวิว" width="128">
</p>

<h1 align="center">LightKub</h1>

<p align="center">
  <b>โปรแกรมจัดคลังรูปและล้างไฟล์ RAW แบบโอเพนซอร์ส เขียนด้วย Rust ทั้งหมด</b><br>
  คัดรูป แต่งแสงสี มาสก์ ครอป จัดอัลบั้ม และส่งออก โดยไม่แตะไฟล์ต้นฉบับ<br>
  macOS · Windows · Linux · FreeBSD · เว็บ
</p>

<p align="center">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-9b4fd8">
  <img alt="Written in Rust" src="https://img.shields.io/badge/written%20in-Rust-4b1a78">
  <img alt="No account, no telemetry" src="https://img.shields.io/badge/no%20account-no%20telemetry-e8692d">
</p>

> [!NOTE]
> LightKub พัฒนาต่อจาก [LightCraft](https://github.com/storytold/lightcraft) ของทีม ArtCraft
> ภายใต้สัญญาอนุญาต MIT OR Apache-2.0 แต่ไม่ได้จัดทำ สนับสนุน หรือรับรองโดยทีม ArtCraft

<p align="center">
  <img src="docs/images/hero-tetons.jpg" alt="หน้าจอแก้ภาพของ LightKub กับภาพ The Tetons and the Snake River ของ Ansel Adams พร้อมแผง Light และ Effects" width="100%">
  <sub><i>Ansel Adams, "The Tetons and the Snake River", 1942 (สาธารณสมบัติ)</i></sub>
</p>

---

## จุดเด่น

- **แต่งภาพแบบไม่ทำลายต้นฉบับ:** ทุกการปรับเก็บเป็นคำสั่ง ย้อนกลับได้เสมอ ไฟล์ต้นฉบับไม่ถูกแก้
- **คุณภาพสีระดับมืออาชีพ:** ประมวลผลแบบ scene-referred, wide-gamut และ float 32 บิต ไฮไลต์ไม่แตก เงาเปิดได้ไม่มีขอบเทา
- **เร็ว:** ใช้ GPU (Metal / Vulkan / DX12) และให้ผลตรงกับ CPU ภายใน 1/255 ไม่มี GPU ก็ใช้ CPU ทุกคอร์
- **เป็นของคุณ:** ไม่ต้องสมัครบัญชี ไม่มีคลาวด์ ไม่ส่งข้อมูลการใช้งาน ไม่มีค่าสมาชิก
- **แสดงภาษาไทยได้:** ชื่อโฟลเดอร์ ไฟล์ คีย์เวิร์ด และคำบรรยายภาพภาษาไทยแสดงด้วยฟอนต์ Anuphan

## ทำอะไรได้บ้าง

| งาน | รายละเอียด |
|---|---|
| แสง | Exposure, Contrast, Highlights, Shadows, Whites, Blacks พร้อม local tone mapping |
| สี | White balance (มี eyedropper), Vibrance, Saturation, Color Mixer 8 สี, Color Grading 3 วง, Calibration, ขาวดำ |
| เอฟเฟกต์ | Texture, Clarity, Dehaze, Vignette, Grain, Tone Curve (แบบ parametric และ point curve) |
| มาสก์ | แปรง, linear, radial, ช่วงความสว่าง/สี, บวก/ลบ/ตัดกัน |
| ครอปและเรขาคณิต | ครอป หมุน ปรับเอียงอัตโนมัติ Upright แก้เลนส์ (distortion, vignetting, CA) |
| รีทัช | ลบจุด heal/clone ตาแดง ตาสัตว์เลี้ยง |
| รวมภาพ | HDR, Panorama, HDR Panorama → DNG |
| คลังรูป | อัลบั้ม โฟลเดอร์ smart album, stack, virtual copy, ดาว, ธง, ป้ายสี, ค้นหาตามฟิลด์ (`rating:>3 iso:>800 keyword:ภูเขา`) |
| นำเข้า | เพิ่มแบบอยู่ที่เดิม/คัดลอก/ย้าย, ตั้งชื่อและโฟลเดอร์ตามแม่แบบ, ตรวจรูปซ้ำ, โฟลเดอร์ที่เฝ้าดู |
| ส่งออก | JPEG / PNG / TIFF / WebP / AVIF / DNG, ปรับขนาด, จำกัดขนาดไฟล์, ลายน้ำ, ส่งออกหลายรูป |
| ไฟล์ RAW | DNG, Canon CR2/CR3, Sony ARW, Nikon NEF, Fujifilm RAF (รวม X-Trans), Panasonic RW2, Pentax PEF, Olympus ORF (ตัวถอดรหัสเขียนเองทั้งหมด) |
| XMP | อ่าน/เขียน sidecar, อ่านค่า `crs:` และไฟล์ preset |

<table>
<tr>
<td width="50%"><img src="docs/images/masking.jpg" alt="แผง Masking กับมาสก์ท้องฟ้าแบบ linear และมาสก์แสงอาทิตย์แบบ radial"><br><sub>มาสก์ท้องฟ้าและแสงอาทิตย์</sub></td>
<td width="50%"><img src="docs/images/grid-demo.jpg" alt="Photo Grid ของรูปตัวอย่าง 24 รูป พร้อมดาวและธง และอัลบั้มซ้อนในโฟลเดอร์"><br><sub>Photo Grid กับอัลบั้มในโฟลเดอร์ <i>คลังรูปตัวอย่าง</i></sub></td>
</tr>
</table>

### ให้ AI agent ควบคุม

ทุกเมนู สไลเดอร์ แปรง และปุ่มลัดเป็น **คำสั่ง** ที่มี id และพารามิเตอร์ JSON ตายตัว
หน้าจอ คีย์บอร์ด CLI ช่องควบคุมแบบ JSON-lines และ **MCP server** ใช้ทางเข้าเดียวกันหมด
agent จึงคัดรูป แต่งภาพ ทำมาสก์ ส่งออก และ *มองเห็น* ผลลัพธ์ได้

```sh
cargo build --release -p lightkub-cli
claude mcp add lightkub -- "$PWD/target/release/lightkub-cli" mcp ~/Pictures/shoot              # แบบไม่เปิดหน้าจอ
claude mcp add lightkub-app -- "$PWD/target/release/lightkub-cli" mcp --connect 127.0.0.1:7980  # คุมโปรแกรมที่เปิดอยู่
lightkub-cli render in.dng -o out.jpg --set light.exposure=0.7
```

รายละเอียดอยู่ใน [docs/mcp.md](docs/mcp.md) และ [docs/control-protocol.md](docs/control-protocol.md)

## โครงสร้างโค้ด

เป็น Cargo workspace ที่แบ่ง crate ตามหน้าที่และบังคับลำดับชั้น (`cargo xtask layers`) โดยแกนหลักไม่ขึ้นกับ UI
(ชื่อ crate ภายในยังเป็น `lightcraft-*` เหมือนต้นฉบับ เพื่อให้ดึงอัปเดตจาก LightCraft ได้ง่าย):

| Crate | หน้าที่ |
|---|---|
| `lightcraft-geom`, `-color`, `-raster`, `-tiff` | เรขาคณิต วิทยาศาสตร์สี บัฟเฟอร์ภาพ TIFF |
| `lightcraft-raw`, `-codecs`, `-meta` | ถอดรหัส RAW ไฟล์ภาพ และ metadata/XMP |
| `lightcraft-develop`, `-pipeline`, `-gpu` | ค่าการแต่งภาพ และ pipeline บน CPU/GPU |
| `lightcraft-catalog`, `-preview` | คลังรูป (log แบบต่อท้ายที่อ่านได้) และ thumbnail |
| `lightcraft-engine` | ส่วนกลางที่ทุก frontend ใช้: คำสั่ง undo การส่งออก |
| `lightcraft-ui-egui`, `-mcp` | หน้าจอ desktop/เว็บ และ MCP server |
| `apps/lightkub`, `apps/lightkub-cli`, `apps/lightkub-web` | ตัวโปรแกรม CLI และเวอร์ชันเว็บ |

## เริ่มต้นใช้งาน

ต้องมี Rust 1.90 ขึ้นไป (บน Windows ต้องมี Visual Studio Build Tools ที่มี C++ ด้วย)

```sh
git clone https://github.com/teh-natsu/lightkub
cd lightkub
cargo run --release -p lightkub     # เปิดคลังรูป (~/Pictures/LightKub Library; คลังใหม่มีรูปตัวอย่างให้)
cargo test --workspace              # รันเทสต์
cargo xtask ci                      # ตรวจทุกอย่างแบบเดียวกับ CI
```

ภาษาของหน้าจอเลือกได้ใน Settings (ดู [docs/localization.md](docs/localization.md))

## สถานะ

ยังเป็นรุ่นทดลอง ใช้กับ JPEG/DNG และไฟล์ RAW ส่วนใหญ่ของ Nikon / Sony / Canon รุ่นเก่าได้ดีแล้ว
ส่วนที่ยังขาดคือการปรับเทียบสีกล้องแบบวัดจริง ไฟล์ RAW บางแบบ (Olympus แบบบีบอัด, CR3 บางรุ่น)
มาสก์และลด noise ด้วย AI และโหมด HDR / วิดีโอ รายละเอียดอยู่ใน [ROADMAP.md](ROADMAP.md) และ [docs/parity.md](docs/parity.md)

## สัญญาอนุญาตและเครดิต

LightKub ใช้สัญญาอนุญาตคู่ [MIT](LICENSE-MIT) หรือ [Apache-2.0](LICENSE-APACHE) เลือกได้ตามต้องการ
(ยกเว้น `crates/segment` ที่เป็น Apache-2.0 อย่างเดียว ดู [NOTICE](NOTICE))
Copyright (c) 2026 Nattpol Chaisri and the LightKub contributors

พัฒนาต่อจาก [LightCraft](https://github.com/storytold/lightcraft),
Copyright (c) 2026 ArtCraft Team and the LightCraft contributors ข้อความที่ต้องแสดงอยู่ใน [NOTICE](NOTICE)

ฟอนต์ ไอคอน และ asset อื่น ๆ ใช้สัญญาอนุญาตแบบเปิดของแต่ละชิ้น รายการพร้อมผู้สร้างและแหล่งที่มาอยู่ใน
[assets/ATTRIBUTION.md](assets/ATTRIBUTION.md) ไอคอนของโปรแกรมอธิบายไว้ใน [assets/app-icon/README.md](assets/app-icon/README.md)

<sub>Adobe and Lightroom are trademarks or registered trademarks of Adobe Inc. in the United States and/or other countries. LightKub is an independent, open-source project and is not affiliated with, sponsored by or endorsed by Adobe Inc.</sub>

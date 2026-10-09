//! Opening web links in the browser (the SAM and model-licence pages, links in photo metadata).
//!
//! LightKub shows no project links in the app: no Help, Feedback, website or GitHub items.

/// Open `url` in the user's browser (through the host's `open_url` service).
pub fn open(app: &mut crate::LightkubApp, url: &str) -> Result<serde_json::Value, String> {
    let open = app.services.open_url.as_mut().ok_or("can't open links here")?;
    open(url)?;
    Ok(serde_json::json!({ "url": url }))
}

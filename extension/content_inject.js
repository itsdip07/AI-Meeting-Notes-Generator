let mediaRecorder;
let audioChunks = [];

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.action === "start_capture") {
    navigator.mediaDevices.getDisplayMedia({ audio: true, video: true })
      .then((stream) => {
        mediaRecorder = new MediaRecorder(stream, { mimeType: "audio/webm" });

        mediaRecorder.ondataavailable = (e) => {
          if (e.data.size > 0) audioChunks.push(e.data);
        };

        mediaRecorder.start(3000);
        sendResponse({ status: "started" });
      })
      .catch((err) => sendResponse({ status: "error", error: err.message }));
    return true;
  }

  if (msg.action === "stop_capture") {
    mediaRecorder.stop();

    mediaRecorder.onstop = async () => {
      const blob = new Blob(audioChunks, { type: "audio/webm" });

      const file = new File([blob], "meeting.webm", { type: "audio/webm" });

      const form = new FormData();
      form.append("file", file);

      await fetch("http://localhost:8000/upload", {
        method: "POST",
        body: form
      });

      audioChunks = [];
    };

    sendResponse({ status: "stopped" });
  }
});

/* Load an optional remote player only when the student chooses a video. */
document.querySelectorAll('[data-video-embed]').forEach(stage => {
  const button = stage.querySelector('button');
  button.addEventListener('click', () => {
    const frame = document.createElement('iframe');
    frame.src = stage.dataset.videoEmbed;
    frame.title = stage.dataset.videoTitle;
    frame.allow = 'accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen';
    frame.allowFullscreen = true;
    frame.referrerPolicy = 'strict-origin-when-cross-origin';
    stage.replaceChildren(frame);
    frame.focus({ preventScroll: true });
  }, { once: true });
});

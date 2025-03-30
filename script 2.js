document.addEventListener('DOMContentLoaded', function() {
  // Select all episode thumbnails
  const episodes = document.querySelectorAll('.episode');
  const modal = document.getElementById('videoModal');
  const videoPlayer = document.getElementById('videoPlayer');
  const closeBtn = document.querySelector('.close');

  // Add click event to each episode thumbnail
  episodes.forEach(function(episode) {
    episode.addEventListener('click', function() {
      // Get the video URL from the data attribute
      const videoUrl = episode.getAttribute('data-video');
      // Set the iframe src to the video URL
      videoPlayer.src = videoUrl;
      // Show the modal
      modal.style.display = 'block';
    });
  });

  // Close the modal when the close button is clicked
  closeBtn.addEventListener('click', function() {
    modal.style.display = 'none';
    videoPlayer.src = '';
  });

  // Close the modal when clicking outside the modal content
  window.addEventListener('click', function(event) {
    if (event.target == modal) {
      modal.style.display = 'none';
      videoPlayer.src = '';
    }
  });
});
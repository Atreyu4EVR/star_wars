// Star Wars Adventure Game JavaScript

document.addEventListener("DOMContentLoaded", function () {
  // Add lightsaber hover effect to buttons
  const buttons = document.querySelectorAll(".btn-primary, .btn-secondary");

  buttons.forEach((button) => {
    button.addEventListener("mouseenter", function () {
      // Play lightsaber sound
      playSound("lightsaber");
    });
  });

  // Add sound effects
  function playSound(soundName) {
    // Check if audio is enabled in localStorage
    const audioEnabled = localStorage.getItem("audioEnabled") !== "false";

    if (!audioEnabled) return;

    let soundPath;
    switch (soundName) {
      case "lightsaber":
        soundPath = "/static/sounds/lightsaber.mp3";
        break;
      case "blaster":
        soundPath = "/static/sounds/blaster.mp3";
        break;
      case "force":
        soundPath = "/static/sounds/force.mp3";
        break;
      default:
        return;
    }

    const audio = new Audio(soundPath);
    audio.volume = 0.3;
    audio.play().catch((e) => console.log("Audio play failed:", e));
  }

  // Add audio toggle button to the page if it doesn't exist
  if (!document.getElementById("audio-toggle")) {
    const audioButton = document.createElement("button");
    audioButton.id = "audio-toggle";
    audioButton.className = "audio-toggle";
    audioButton.innerHTML = '<i class="fas fa-volume-up"></i>';
    audioButton.title = "Toggle Sound Effects";

    // Set initial state based on localStorage
    const audioEnabled = localStorage.getItem("audioEnabled") !== "false";
    if (!audioEnabled) {
      audioButton.innerHTML = '<i class="fas fa-volume-mute"></i>';
      audioButton.classList.add("muted");
    }

    audioButton.addEventListener("click", function () {
      const isCurrentlyEnabled =
        localStorage.getItem("audioEnabled") !== "false";
      localStorage.setItem("audioEnabled", !isCurrentlyEnabled);

      if (isCurrentlyEnabled) {
        audioButton.innerHTML = '<i class="fas fa-volume-mute"></i>';
        audioButton.classList.add("muted");
      } else {
        audioButton.innerHTML = '<i class="fas fa-volume-up"></i>';
        audioButton.classList.remove("muted");
        // Play a sound to confirm it's working
        playSound("lightsaber");
      }
    });

    document.body.appendChild(audioButton);
  }

  // Add parallax effect to background
  document.addEventListener("mousemove", function (e) {
    const stars = document.querySelector(".stars");
    const twinkling = document.querySelector(".twinkling");

    if (stars && twinkling) {
      const x = e.clientX / window.innerWidth;
      const y = e.clientY / window.innerHeight;

      stars.style.transform = `translate(${x * 10}px, ${y * 10}px)`;
      twinkling.style.transform = `translate(${x * 20}px, ${y * 20}px)`;
    }
  });

  // Add loading screen effect when navigating between pages
  const links = document.querySelectorAll("a");
  const forms = document.querySelectorAll("form");

  function createLoadingScreen() {
    const loadingScreen = document.createElement("div");
    loadingScreen.className = "loading-screen";
    loadingScreen.innerHTML = `
            <div class="loading-content">
                <img src="/static/images/lightsaber_loading.gif" alt="Loading...">
                <p>Traveling through hyperspace...</p>
            </div>
        `;
    document.body.appendChild(loadingScreen);

    setTimeout(() => {
      loadingScreen.classList.add("active");
    }, 10);
  }

  links.forEach((link) => {
    link.addEventListener("click", function (e) {
      // Don't show loading screen for external links or javascript links
      if (
        this.getAttribute("href").startsWith("#") ||
        this.getAttribute("href").startsWith("javascript:") ||
        this.getAttribute("target") === "_blank"
      ) {
        return;
      }

      e.preventDefault();
      createLoadingScreen();

      setTimeout(() => {
        window.location.href = this.getAttribute("href");
      }, 1000);
    });
  });

  forms.forEach((form) => {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      createLoadingScreen();

      setTimeout(() => {
        this.submit();
      }, 1000);
    });
  });
});

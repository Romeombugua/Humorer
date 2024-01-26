
document.addEventListener('DOMContentLoaded', function () {
    var shareButton = document.getElementById('shareButton');
    var shareUrlElement = document.getElementById('shareUrl');

    shareButton.addEventListener('click', function () {
        var videoUrl = "{% url 'shareable_video_url' video.id %}";
        copyToClipboard(videoUrl);
        shareUrlElement.innerHTML = 'URL copied to clipboard: ' + videoUrl;
    });

    function copyToClipboard(text) {
        var textarea = document.createElement('textarea');
        textarea.value = text;
        textarea.setAttribute('readonly', '');
        textarea.style.position = 'absolute';
        textarea.style.left = '-9999px';
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
    }
});


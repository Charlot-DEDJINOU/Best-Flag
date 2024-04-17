export const Redirect = (url) => {
    if (url !== '') {
        window.open(url, '_blank')
      }
}

export function downloadImage(imageName, imageUrl) {
  var downloadLink = document.createElement('a');
  downloadLink.href = imageUrl;
  downloadLink.download = imageName;

  document.body.appendChild(downloadLink);

  downloadLink.click();

  document.body.removeChild(downloadLink);
}


import pdfPathFr from '../data/Charlot_DEDJINOU_Fr.pdf'
import pdfPathEn from '../data/Charlot_DEDJINOU_En.pdf'

export function downloadCV(locale) {
  const link = document.createElement('a')
  link.download = 'Charlot_DEDJINOU_CV.pdf'
  link.href = locale === 'fr' ? pdfPathFr : pdfPathEn

  link.click()
}

export function Forward(urlDuSite) {
  if (urlDuSite !== '') {
    window.open(urlDuSite, '_blank')
  }
}
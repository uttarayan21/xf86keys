# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# Maintainer: Your Name <uttarayan21@gmail.com>
pkgname=xf86keys
pkgver=v1.0
pkgrel=1
epoch=
pkgdesc="Control Both MPD MPRIS2 music players"
arch=('any')
url="https://github.com/uttarayan21/xf86keys"
license=('GPL')
groups=()
depends=('python-dbus' 'python-pynput' 'python-mpd2')
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=${pkgname}.install
changelog=
source=("${pkgname}-${pkgver}.tar.gz::https://codeload.github.com/uttarayan21/${pkgname}/tar.gz/${pkgver}")
noextract=()
md5sums=('e68116928caf5487e1243e8d11a236c0')
validpgpkeys=()

# prepare() {
# 	cd "$pkgname-$pkgver"
# }

# build() {
# 	cd "$pkgname-$pkgver"
# }

# check() {
# 	cd "$pkgname-$pkgver"
# 	make -k check
# }

package() {
  echo $srcdir
  echo $pkgdir
	cd "${srcdir}"
	# make DESTDIR="$pkgdir/" install
  echo "Extracting ${pkgname}-${pkgver}.tar.gz"
  tar -vxf ${pkgname}-${pkgver}.tar.gz
  install -Dm755 "${srcdir}/${pkgname}-1.0/xf86keys.py" "${pkgdir}/usr/bin/xf86keys"
	install -Dm644 "${srcdir}/${pkgname}-1.0/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

}

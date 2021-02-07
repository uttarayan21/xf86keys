# Maintainer: Uttarayan Mondal <uttarayan21@gmail.com>
pkgname=xf86keys
pkgver=v1.1
pkgrel=1
epoch=
pkgdesc="keybinds both MPD MPRIS2 music players"
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
source=("${pkgname}::git+git://github.com/uttarayan21/xf86keys.git")
noextract=()
md5sums=('SKIP')
validpgpkeys=()

package() {
    install -Dm755 "${srcdir}/${pkgname}/xf86keys.py" "${pkgdir}/usr/bin/xf86keys"
    install -Dm644 "${srcdir}/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

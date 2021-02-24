# Maintainer: Uttarayan Mondal <uttarayan21@gmail.com>
pkgname=xf86keys
pkgver=v1.5
pkgrel=3
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
    sitepkg="$(python -c 'from distutils.sysconfig import get_python_lib; print(get_python_lib())')"
    install -Dm755 "${srcdir}/${pkgname}/main.py"   "${pkgdir}/usr/bin/xf86keys"
    install -Ddm755 "${srcdir}/${pkgname}/xf86keys"      "${pkgdir}/${sitepkg}/xf86keys"
    cd "${pkgname}"
    for file in xf86keys/*;do
        install -Dm644 "${file}"                        "${pkgdir}/${sitepkg}/${file}"
    done
    install -Dm644 "${srcdir}/${pkgname}/LICENSE"       "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

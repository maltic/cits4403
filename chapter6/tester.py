import CA
import CADrawer

rule  = 30
n = 500

ca = CA.CA(rule, n)
ca.start_single()
ca.loop(n-1)

drawer = CADrawer.PyplotDrawer()
drawer.draw(ca)
drawer.show()
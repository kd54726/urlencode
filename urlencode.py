#python 3.7.1

def urlencode(inp):
  str = inp
 
  n3 = str.replace('3' , '%33')
  n0 = n3.replace('0' , '%30')
  n1 = n0.replace('1' , '%31')
  n2 = n1.replace('2' , '%32')
  n4 = n2.replace('4' , '%34')
  n5 = n4.replace('5' , '%35')
  n6 = n5.replace('6' , '%36')
  n7 = n6.replace('7' , '%37')
  n8 = n7.replace('8' , '%38')
  n9 = n8.replace('9' , '%39')
  A = n9.replace('A' , '%41')
  B = A.replace('B' , '%42')
  C = B.replace('C' , '%43')
  D = C.replace('D' , '%44')
  E = D.replace('E' , '%45')
  F = E.replace('F' , '%46')
  G = F.replace('G' , '%47')
  H = G.replace('H' , '%48')
  I = H.replace('I' , '%49')
  J = I.replace('J' , '%4A')
  K = J.replace('K' , '%4B')
  L = K.replace('L' , '%4C')
  M = L.replace('M' , '%4D')
  N = M.replace('N' , '%4E')
  O = N.replace('O' , '%4F')
  P = O.replace('P' , '%50')
  Q = P.replace('Q' , '%51')
  R = Q.replace('R' , '%52')
  S = R.replace('S' , '%53')
  T = S.replace('T' , '%54')
  U = T.replace('U' , '%55')
  V = U.replace('V' , '%56')
  W = V.replace('W' , '%57')
  X = W.replace('x' , '%58')
  Y = X.replace('Y' , '%59')
  Z = Y.replace('Z' , '%5A')
  a = Z.replace('a' , '%61')
  b = a.replace('b' , '%62')
  c = b.replace('c' , '%63')
  d = c.replace('d' , '%64')
  e = d.replace('e' , '%65')
  f = e.replace('f' , '%66')
  g = f.replace('g' , '%67')
  h = g.replace('h' , '%68')
  i = h.replace('i' , '%69')
  j = i.replace('j' , '%6A')
  k = j.replace('k' , '%6B')
  l = k.replace('l' , '%6C')
  m = l.replace('m' , '%6D')
  n = m.replace('n' , '%6E')
  o = n.replace('o' , '%6F')
  p = o.replace('p' , '%70')
  q = p.replace('q' , '%71')
  r = q.replace('r' , '%72')
  s = r.replace('s' , '%73')
  t = s.replace('t' , '%74')
  u = t.replace('u' , '%75')
  v = u.replace('v' , '%76')
  w = v.replace('w' , '%77')
  x = w.replace('x' , '%78')
  y = x.replace('y' , '%79')
  z = y.replace('z' , '%7A')
  vv = z.replace('{' , '%7B')
  ww = vv.replace('|' , '%7C')
  xx = ww.replace('}' , '%7D')
  yy = xx.replace('~' , '%7E')
  zz = yy.replace('`' , '%E2%82%AC')
  aa = zz.replace(' ' , '%20')
  bb = aa.replace('!' , '%21') 
  cc = bb.replace('"' , '%22')
#  hd = dq.replace('#' , '%23')
  dd = cc.replace('$' , '%24')
  ee = dd.replace('&' , '%26')
  ff = ee.replace("'" , "%27")
  gg = ff.replace('(' , '%28')
  hh = gg.replace(')' , '%29')
  ii = hh.replace('*' , '%2A')
  jj = ii.replace('+' , '%2B')
  kk = jj.replace(',' , '%2C')
  ll = kk.replace('-' , '%2D')
  mm = ll.replace('.' , '%2E')
  nn = mm.replace('/' , '%2F')
  oo = nn.replace(':' , '%3A')
  pp = oo.replace(';' , '%3B')
  qq = pp.replace('<' , '%3C')
  rr = qq.replace('=' , '%3D')
  ss = rr.replace('>' , '%3E')
  tt = ss.replace('?' , '%3F')
  uu = tt.replace('@' , '%40')
 # pe = uu.replace('%' , '%25')
 
  print("\n")
  print(uu)

urlencode(inp = input('Text to Encode: '))

inp2 = "y"
while inp2 == 'y':
  urlencode(inp = input('\nText to Encode: '))
else:
    print("\ndone")
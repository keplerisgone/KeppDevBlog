# Effect of Noise in Communication Systems

신호에 생긴 노이즈가 어떤 영향을 끼치는지 알아보자. 주로 노이즈는 보내진 신호에 더해져 보내지며, 이를 **Additive white Gaussian Noise**라고 한다. 따라서 받는 신호의 수식은 다음과 같다.
$$
r(t) = s(t) + w(t) (=n(t))
$$
이 때 $r(t)$는 받는 전체 신호이고, $s(t)$는 보낸 신호, $n(t)$는 노이즈이다. 아날로그 통신 체계의 가장 주가 되는 문제가 바로 노이즈를 처리하는 것이다. 이를 얼마나 잘 처리하는지는 보낸 신호와 노이즈의 power 비로 나타낼 수 있으며, **Signal to Noise Ratio**(SNR)라고 한다. (${S\over N} = {E[s^{2}(t)]\over E[n^{2}(t)]}$)

AM같은 경우, Coherent detection를 사용하는 경우 Oscillator를 사용하고, 사용하지 않는 경우는 envelope detector(Diode-RC)를 사용한다. 이 때는 Performance panalty가 존재.

FM 같은 경우는 애초에 Nonlinear한 시스템이기 때문에 noise 또한 nonlinear한 형태가 된다. plat한 노이즈가 들어와도 결과적으로는 parabolic noise가 된다. Bandwidth가 높아질수록 noise에 대한 저항력이 커진다.

# Bandpass Signals



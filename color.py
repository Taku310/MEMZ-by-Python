import ctypes

# 必要な定数や関数の定義
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# モニターのデバイスコンテキスト取得
hdc = user32.GetDC(0)

# モニターの解像度取得
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

# 画面全体を反転させる
gdi32.BitBlt(hdc, 0, 0, width, height, hdc, 0, 0, 0x00550009)

# 後処理
user32.ReleaseDC(0, hdc)


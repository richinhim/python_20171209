daum = 89000
naver = 751000

daum_stock = 100
naver_stock = 20

daum_total = daum * daum_stock
naver_total = naver * naver_stock

print("주식 총액: ", daum_total + naver_total)

daum_loss = 0.05
naver_loss = 0.1

daum_loss_total = daum_total * daum_loss
naver_loss_total = naver_total * naver_loss

print("손실액:", daum_loss_total + naver_loss_total)
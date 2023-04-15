import argparse
import datetime
import twder

USDtoTWD = float(twder.now('USD')[2])
year = datetime.date.today().year

parser = argparse.ArgumentParser(description='計算債券預估年獲利率')
parser.add_argument('--couponRate', type=float, default = None, help='輸入票面利率')
parser.add_argument('--buy', type=float, default = None, help='輸入申購價')
parser.add_argument('--sell', type=float, default = None, help='輸入預估售出價')
parser.add_argument('--years', type=float, default = None, help='輸入到期年')
parser.add_argument('--faceValue', type=int, default = 10000, help='輸入票面金額，預設為10000')
args = parser.parse_args()

if not args.couponRate:
    print('請輸入票面利率')
    exit()
if not args.buy:
    print('請輸入申購金額')
    exit()
if not args.sell:
    print('請輸入預估售出價')
    exit()
if not args.years:
    print('請輸入到期年')
    exit()

#每年利息
interest = args.couponRate * args.faceValue
years = args.years - year
# [(票面利率*年數*票面金額+預估售出價格-購入成本)/年數]*100 % = 預估年獲利率
expectedRate = ((years * interest + args.sell - args.buy) / years) * 0.01

print('預估年獲利率： ' + str(expectedRate) + '% 每年利息： ' +  str(interest) + '美元 大約: ' + str(interest * USDtoTWD) + '台幣')
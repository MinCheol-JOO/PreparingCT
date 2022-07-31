    def reverseBits(self, n):
        n = bin(n)[2:]         # convert to binary, and remove the usual 0b prefix
        print(n)                # 여기서 0b를 없애기 위함
        n = '%32s' % n         # print number into a pre-formatted string with space-padding
        print(n)                # 32개만들고 우측부터 정렬을 시켰습니다.
        n = n.replace(' ','0') # Convert the useful space-padding into zeros
        print(n)
        # Now we have a  proper binary representation, so we can make the final transformation
        return int(n[::-1],2)
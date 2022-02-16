# we will move outwards, left and right from a middle pointer to make sure substring is palindrome
# time complexity O(n^2)
class Solution:
    def getPalindrome(self, s, sLength, l, r):
        palindromicString = ''
        palindromeLength = sLength
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > palindromeLength:
                palindromicString = s[l:r+1]
                palindromeLength = r - l + 1
            l -= 1
            r += 1
            
        return {"palindrome": palindromicString, "palindromeLength": palindromeLength}
    
    def longestPalindrome(self, s: str) -> str:
        palindromicString = ''
        palindromeLength = 0
        
        for i in range(len(s)):
            # handling odd length string
            l, r = i, i
            
            response = self.getPalindrome(s, palindromeLength, l, r)

            if response['palindrome'] != '':
                palindromicString = response['palindrome']
                palindromeLength = response['palindromeLength']
                
            # handling even length string
            l, r = i, i+1
            
            response = self.getPalindrome(s, palindromeLength, l, r)

            if response['palindrome'] != '':
                palindromicString = response['palindrome']
                palindromeLength = response['palindromeLength']             
                        
        return palindromicString


# inputString = "babad"
# inputString = "aacabdkdacaa"

# inputString = "ibawpzhrunsgfobmenlqlxnprtgijgbeicsuoihnmcekzmvtffmlpzuwlimuuzjhkzppmpqqrfwyrjrsltkypjpcjffpvhtdiwjdonutobpecsiqubiusvwsyhrddqjeqqpgofifmwvmcdjixjvjxrvyabqaqumfqiiqxizmhzevhxutsbgzcfggyyvolwaxfcpjhfpksxvgyxhddcssnxhygzvmyxrxqizzhpluxkautjmieximoskcffimctsfzgmihtoxkltopwobtfjvjymtuknxmsgevkeklprcaudidywwkfuhtatpeeiewczpwiegmpjquayfleczrvzekikbaeocpcurtxhcsysbbsyschxtrucpcoeabkikezvrzcelfyauqjpmgeiwpzcweieeptathufkwwydiduacrplkekvegsmxnkutmyjvjftbowpotlkxothimgzfstcmiffcksomixeimjtuakxulphzziqxrxymvzgyhxnsscddhxygvxskpfhjpcfxawlovyyggfczgbstuxhvezhmzixqiiqfmuqaqbayvrxjvjxijdcmvwmfifogpqqejqddrhyswvsuibuqiscepbotunodjwidthvpffjcpjpyktlsrjrywfrqqpmppzkhjzuumilwuzplmfftvmzkecmnhiousciebgjigtrpnxlqlnembofgsnurhzpwabi"
inputString = "uhrfjotnewtodhmbplsaolnpcdaohiytmfllukijouxipvqohtsgxbtfoxyfkfczkfwhzimbefiohmtimrcxbpgcxogystdkcqujvbxsgirpccdnvejtljftwkdpsqpflzwruwwdzovsbmwbcvlftkjnxqaguvtsycylqzquqkbnybnbaeahbxejhphwrpmymcemuhljwtuvxefqfzjhskuqhifydkxpnfwfxkpeexnjltfqwfvchphmtsrsyayxukvmlqodshqwbeaxhcxdbssnrdzvxtusngwqdxvluauphmmbwmgtazjwvolenegwbmjfwprfuswamyvgrgshqocnhirgyakbkkggviorawadzhjipjjgiwpelwxvtaegauerbwpalofrbghfhnublttqtcmqskcocwwwxpnckrnbepusjyohsrretrqyvgnbezuvwmzizcefxyumtdwnqjkgsktyuacfpnqocqjxcurmipjfqmjqrkdeqsfseyigqlwmzgqhivbqalcxhlzgtsfjbdbfqiedogrqasgmimifdexbjjpfusxsypxobxjtcwxnkpgkdpgskgkvezkriixpxkkattyplnpdbdifforxozfngmlgcunbnubzamgkkfbswuqfqrvzjqmlfqxeqpjaqayodtetsecmfbplscmslpqiyhhykftzkkhshxqvdwmwowokpluwyvavwvofwqtdilwqjgrprukzyhckuspyzaoe"
# Run time = 6932 ms !!

# print(len(inputString))

solutionString = Solution()
result = solutionString.longestPalindrome(inputString)

if result is not None: 
    print(len(result))
    print(f"[{result}] < == is the Palindrom substring of the string ==> [{inputString}]")
else: print(f"No Palindrom substring found for the string ==> [{inputString}]")
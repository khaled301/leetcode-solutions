class Solution:
    def longestPalindrome(self, s: str) -> str:
        forwardString = None
        reverseString = None
        palindromicString = None
        
        if len(s) == 1:
            return s 
        elif s is None:
            return '' 
        
        charCount = 0
        
        while charCount < len(s):
            tempString = ''
            
            if palindromicString is not None and (len(palindromicString) == len(s) or len(palindromicString) >= (len(s)-charCount)): 
                return palindromicString
            
            for i in range(charCount, len(s), 1):
                
                # print(i)
                tempString = tempString + s[i]
                forwardString = tempString 
                reverseString = tempString[::-1]       
                
                if forwardString == reverseString and (palindromicString is None or len(forwardString) > len(palindromicString)):
                    palindromicString = forwardString
                    
            charCount += 1
                        
        return palindromicString


# inputString = "babad"
inputString = "aacabdkacaa"

# inputString = "ibawpzhrunsgfobmenlqlxnprtgijgbeicsuoihnmcekzmvtffmlpzuwlimuuzjhkzppmpqqrfwyrjrsltkypjpcjffpvhtdiwjdonutobpecsiqubiusvwsyhrddqjeqqpgofifmwvmcdjixjvjxrvyabqaqumfqiiqxizmhzevhxutsbgzcfggyyvolwaxfcpjhfpksxvgyxhddcssnxhygzvmyxrxqizzhpluxkautjmieximoskcffimctsfzgmihtoxkltopwobtfjvjymtuknxmsgevkeklprcaudidywwkfuhtatpeeiewczpwiegmpjquayfleczrvzekikbaeocpcurtxhcsysbbsyschxtrucpcoeabkikezvrzcelfyauqjpmgeiwpzcweieeptathufkwwydiduacrplkekvegsmxnkutmyjvjftbowpotlkxothimgzfstcmiffcksomixeimjtuakxulphzziqxrxymvzgyhxnsscddhxygvxskpfhjpcfxawlovyyggfczgbstuxhvezhmzixqiiqfmuqaqbayvrxjvjxijdcmvwmfifogpqqejqddrhyswvsuibuqiscepbotunodjwidthvpffjcpjpyktlsrjrywfrqqpmppzkhjzuumilwuzplmfftvmzkecmnhiousciebgjigtrpnxlqlnembofgsnurhzpwabi"
# Run time = 6932 ms !!

# print(len(inputString))

solutionString = Solution()
result = solutionString.longestPalindrome(inputString)

if result is not None: 
    print(len(result))
    print(f"[{result}] is the Palindrom substring of the string [{inputString}]")
else: print(f"No Palindrom substring found for the string [{inputString}]")
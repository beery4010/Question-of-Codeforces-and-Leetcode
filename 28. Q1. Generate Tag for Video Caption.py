class Solution:
    def generateTag(self, caption: str) -> str:
        split_input = caption.strip().split(" ")
        output = ["#"]*(len(split_input) + 1)
        count  = 0

        for i in split_input:
            if count == 0:
                output[count + 1] = i.lower()
                count += 1
            else:
                output[count + 1] = i.capitalize()
                count += 1
        return "".join(output)[:100]

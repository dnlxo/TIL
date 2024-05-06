class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_split = version1.split('.')
        version2_split = version2.split('.')

        version1_split_to_int = [int(i) for i in version1_split]
        version2_split_to_int = [int(i) for i in version2_split]
        max_len = max(len(version1_split_to_int), len(version2_split_to_int))

        for i in range(max_len-len(version1_split_to_int)):
            version1_split_to_int.append(0)
        for i in range(max_len-len(version2_split_to_int)):
            version2_split_to_int.append(0)

        for i in range(max_len):
            if version1_split_to_int[i] > version2_split_to_int[i]:
                return 1
            elif version1_split_to_int[i] < version2_split_to_int[i]:
                return -1
        return 0
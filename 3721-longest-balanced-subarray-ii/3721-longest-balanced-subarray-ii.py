for (int i = 0; i < n; i++) {
        Set<Integer> distinctEvens = new HashSet<>();
        Set<Integer> distinctOdds = new HashSet<>();

        for (int j = i; j < n; j++) {
            int currentNum = nums[j];

            if (currentNum % 2 == 0) {
                distinctEvens.add(currentNum);
            } else {
                distinctOdds.add(currentNum);
            }

            if (distinctEvens.size() == distinctOdds.size()) {
                maxLength = Math.max(maxLength, j - i + 1);
            }
        }
    }

    return maxLength;
}
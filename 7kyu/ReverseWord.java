public class Kata {
    public static String reverseWords(final String original) {
        if (original.trim().length() == 0)
            return original;
        String joined = "";
        for (String word : original.split(" ")) {
            joined += new StringBuilder(word).reverse().toString() + " ";
        }
        return joined.substring(0, joined.length() - 1);
    }
}

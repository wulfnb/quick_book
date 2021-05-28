try {
    File file = new File("fubars.txt");
    FileWriter fw = new FileWriter(file, true);
    PrintWriter pw = new PrintWriter(fw);
    pw.println(arrayToPrint.toString());
} catch (IOException e) {
    e.printStackTrace();
} finally {
    // 
}
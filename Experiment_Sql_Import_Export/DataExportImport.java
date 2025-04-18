import java.sql.*;

public class DataExportImport {
    // Put all your database credentials here
    private static final String URL = "jdbc:sqlserver://localhost:1433;databaseName=YourDatabase";
    private static final String USER = "yourUsername";
    private static final String PASSWORD = "yourPassword";

    // For export
    public static void exportData() {
        String sql = "SELECT * FROM YourTable";
        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                System.out.println("Exported: " + rs.getString("columnName"));
                // Add logic to save to file or another system
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // For import
    public static void importData() {
        String sql = "INSERT INTO YourTable (columnName) VALUES (?)";
        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, "Imported Data");
            pstmt.executeUpdate();
            System.out.println("Data imported successfully");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Main basically calling the created functions(exportData and importData here)
    public static void main(String[] args) {
        exportData();
        importData();
    }
}
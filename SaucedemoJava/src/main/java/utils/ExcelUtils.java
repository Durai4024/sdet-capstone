package utils;

import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileInputStream;
import java.util.*;

public class ExcelUtils {
    public static List<Map<String, String>> getTestData(String path, String sheetName) throws Exception {
        List<Map<String, String>> dataList = new ArrayList<>();
        FileInputStream fis = new FileInputStream(path);
        Workbook workbook = new XSSFWorkbook(fis);
        Sheet sheet = workbook.getSheet(sheetName);

        Row headerRow = sheet.getRow(0);
        for (int i = 1; i <= sheet.getLastRowNum(); i++) {
            Map<String, String> map = new HashMap<>();
            Row row = sheet.getRow(i);
            for (int j = 0; j < row.getLastCellNum(); j++) {
                map.put(headerRow.getCell(j).getStringCellValue(), row.getCell(j).getStringCellValue());
            }
            dataList.add(map);
        }
        workbook.close();
        return dataList;
    }
}
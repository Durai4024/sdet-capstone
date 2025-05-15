package tests;

import base.BaseTest;
import org.testng.Assert;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import pages.ProductsPage;
import pages.LoginPage;
import utils.ExcelUtils;

import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class LoginTest extends BaseTest {

    @DataProvider(name = "LoginData")
    public Iterator<Object[]> getData() throws Exception {
        List<Map<String, String>> data = ExcelUtils.getTestData("TestData/LoginData.xlsx", "Sheet1");
        return data.stream().map(m -> new Object[]{m}).iterator();
    }

    @Test(dataProvider = "LoginData")
    public void testLogin(Map<String, String> data) {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.login(data.get("username"), data.get("password"));

        if (data.get("expectedResult").equals("Swag Labs")) {
            ProductsPage inventoryPage = new ProductsPage(driver);
            Assert.assertEquals(inventoryPage.getTitle(), data.get("expectedResult"));
        } else {
            Assert.assertTrue(loginPage.getErrorMessage().contains(data.get("expectedResult")));
        }
    }
}

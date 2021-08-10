Jmeter 引用代码变量

```java

//source("C:\\Users\\liul8\\Downloads\\BaseTest.java");
//log.info(BaseTest.encode());
	
import java.io.FileInputStream;
import java.io.File;
import java.util.Base64;
import java.net.URLEncoder;

File file = new File("C:\\diy\\old coding\\test\\locust demo\\python-manual\\recognize_images_num\\33.png");
FileInputStream fileInputStreamReader = new FileInputStream(file);
byte[] bytes = new byte[(int)file.length()];
fileInputStreamReader.read(bytes);
String imgStr = Base64.getEncoder().encodeToString(bytes);
String imgParam  = URLEncoder.encode(imgStr, "UTF-8");
log.info("############content##################");
log.info(imgParam );
vars.put("image",imgParam );



import java.io.FileInputStream;  
import java.net.URLEncoder;

String content = null;  
String filePath = "C:\\diy\\old coding\\test\\locust demo\\python-manual\\recognize_images_num\\33.png";
try {  
  FileInputStream fileForInput = new FileInputStream(filePath);  
  byte[] bytes = new byte[fileForInput.available()];  
  fileForInput.read(bytes);  
  content = new sun.misc.BASE64Encoder().encode(bytes); // 具体的编码方法  
  fileForInput.close();  
  log.info("############content##################");
  String imgParam  = URLEncoder.encode(content, "UTF-8");
  log.info(imgParam);
  vars.put("image",imgParam);
} catch (Exception e) {  
	log.info("############exception##################");
  e.printStackTrace();  
}  
```


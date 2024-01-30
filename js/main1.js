//非常暴力的循环模式
//没有做好客制化的准备
//如果需要移植或更改
//请把http://10.0.2.2:5000/photo 改成你的服务器后端
//
//申请权限
if(!requestScreenCapture(false)){
    toast("请求截图失败");
    exit();
}
//设置大小
setScreenMetrics(1920, 1080);
// 暴力塞进循环
setInterval(function(){
toastLog("等待20秒");
sleep(20000);
//1档
sleep(2000);
click(695, 351);
toastLog("3秒后截图");
sleep(3000);
//截图1
var simg1 = captureScreen();
images.save(simg1, "/sdcard/simg1.png");
//上传1
ups1();
function ups1(){
    var res = http.postMultipart("http://10.0.2.2:5000/photo", {
        "file": open("/sdcard/simg1.png")
    });
    log("upload:");
    log(res.body.string());
};
//2档
sleep(2000);
click(898, 351);
toastLog("3秒后截图");
sleep(3000);
//截图2
var simg2 = captureScreen();
images.save(simg2, "/sdcard/simg2.png");
//上传2
ups2();
function ups2(){
    var res = http.postMultipart("http://10.0.2.2:5000/photo", {
        "file": open("/sdcard/simg2.png")
    });
    log("upload:");
    log(res.body.string());
};
//3档
sleep(2000);
click(1099, 351);
toastLog("3秒后截图");
sleep(3000);
//截图3
var simg3 = captureScreen();
images.save(simg3, "/sdcard/simg3.png");
//上传
ups3();
function ups3(){
    var res = http.postMultipart("http://10.0.2.2:5000/photo", {
        "file": open("/sdcard/simg3.png")
    });
    log("upload:");
    log(res.body.string());
};
//4档
sleep(2000);
click(1306, 351);
toastLog("3秒后截图");
sleep(3000);
//截图4
var simg4 = captureScreen();
images.save(simg4, "/sdcard/simg4.png");
//上传
ups4();
function ups4(){
    var res = http.postMultipart("http://10.0.2.2:5000/photo", {
        "file": open("/sdcard/simg4.png")
    });
    log("upload:");
    log(res.body.string());
};
//换难度
sleep(2000);
click(1630, 351);
//tm
sleep(2000);
click(850, 581);
//确定
sleep(2000);
click(1148, 833);
toastLog("3秒后截图");
sleep(3000);
//截图TM
var simgtm = captureScreen();
images.save(simgtm, "/sdcard/simgtm.png");
//上传
upstm();
function upstm(){
    var res = http.postMultipart("http://10.0.2.2:5000/photo", {
        "file": open("/sdcard/simgtm.png")
    });
    log("upload:");
    log(res.body.string());
};
//换难度
sleep(2000);
click(1630, 351);
//ins
sleep(2000);
click(542, 579);
//确定
sleep(2000);
click(1148, 833);
toastLog("3秒后截图");
sleep(3000);
//截图ins
var simgins = captureScreen();
images.save(simgins, "/sdcard/simgins.png");
//上传
upsins();
function upsins(){
    var res = http.postMultipart("http://10.0.2.2:5000/photo", {
        "file": open("/sdcard/simgins.png")
    });
    log("upload:");
    log(res.body.string());
};
//换难度
sleep(2000);
click(1630, 351);
//ex
sleep(2000);
click(1156, 467);
//确定
sleep(2000);
click(1148, 833);
toastLog("3秒后截图");
sleep(3000);
//截图ex
var simgex = captureScreen();
images.save(simgex, "/sdcard/simgex.png");
//上传
upsex();
function upsex(){
    var res = http.postMultipart("http://10.0.2.2:5000/photo", {
        "file": open("/sdcard/simgex.png")
    });
    log("upload:");
    log(res.body.string());
};
toastLog("O");
toastLog("等待40秒");
}, 40000);
toastLog("等待40秒");

package app.eversage.offline;
import android.content.*;import android.app.*;
public class DailyReceiver extends BroadcastReceiver {
 public void onReceive(Context c,Intent i){if(android.os.Build.VERSION.SDK_INT>=33&&c.checkSelfPermission("android.permission.POST_NOTIFICATIONS")!=android.content.pm.PackageManager.PERMISSION_GRANTED)return;NotificationManager n=(NotificationManager)c.getSystemService(Context.NOTIFICATION_SERVICE);n.createNotificationChannel(new NotificationChannel("daily","Daily wisdom",NotificationManager.IMPORTANCE_DEFAULT));PendingIntent p=PendingIntent.getActivity(c,0,new Intent(c,NativeActivity.class).putExtra("daily",true),PendingIntent.FLAG_UPDATE_CURRENT|PendingIntent.FLAG_IMMUTABLE);n.notify(1,new Notification.Builder(c,"daily").setSmallIcon(android.R.drawable.ic_menu_view).setContentTitle("Daily wisdom").setContentText("Read today’s story in EverSage.").setContentIntent(p).setAutoCancel(true).build());}
}

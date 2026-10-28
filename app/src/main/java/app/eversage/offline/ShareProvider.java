package app.eversage.offline;
import android.content.*;import android.database.*;import android.net.Uri;import android.os.*;import java.io.*;
public class ShareProvider extends ContentProvider {
 public boolean onCreate(){return true;}public String getType(Uri u){return "image/png";}
 public ParcelFileDescriptor openFile(Uri u,String mode)throws FileNotFoundException{if(!"/wisdom.png".equals(u.getPath())||!"r".equals(mode))throw new FileNotFoundException();return ParcelFileDescriptor.open(new File(getContext().getCacheDir(),"shared/wisdom.png"),ParcelFileDescriptor.MODE_READ_ONLY);}
 public Cursor query(Uri u,String[] p,String s,String[] a,String order){MatrixCursor c=new MatrixCursor(new String[]{"_display_name","_size"});File f=new File(getContext().getCacheDir(),"shared/wisdom.png");c.addRow(new Object[]{"EverSage-wisdom.png",f.length()});return c;}
 public Uri insert(Uri u,ContentValues v){throw new UnsupportedOperationException();}public int update(Uri u,ContentValues v,String s,String[] a){throw new UnsupportedOperationException();}public int delete(Uri u,String s,String[] a){throw new UnsupportedOperationException();}
}

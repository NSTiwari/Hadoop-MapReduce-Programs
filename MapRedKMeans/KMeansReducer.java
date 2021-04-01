
import java.io.IOException;
import java.util.*;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class KMeansReducer extends Reducer <Text, Text, Text, Text> {
  
  // put any private data structured you need here!
  
  public void reduce (Text key, Iterable <Text> values, Context context) throws IOException, InterruptedException {
    
    // put your code here!
  }
  
  protected void cleanup (Context context) throws IOException, InterruptedException {
    
    // put your code here!
  }
}


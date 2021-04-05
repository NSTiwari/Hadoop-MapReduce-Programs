
import java.io.IOException;
import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;

public class KMeansMapper extends Mapper <LongWritable, Text, Text, Text> {
  
  // this is the list of current clusters
  private ArrayList <VectorizedObject> oldClusters = new ArrayList <VectorizedObject> (0);
  
  // this is the list of clusters that come out of the current iteration
  private ArrayList <VectorizedObject> newClusters = new ArrayList <VectorizedObject> (0);
  
  // this is called to set up the mapper... it basically just reads the clusters file into memory
  protected void setup (Context context) throws IOException, InterruptedException {
    
    // first we open up the clusters file
    Configuration conf = context.getConfiguration ();
    FileSystem dfs = FileSystem.get (conf);
    
    // if we can't find it in the configuration, then die
    if (conf.get ("clusterInput") == null)
      throw new RuntimeException ("no cluster file!");
    
    // create a BufferedReader to open up the cluster file
    Path src = new Path (conf.get ("clusterInput"));
    FSDataInputStream fs = dfs.open (src);
    BufferedReader myReader = new BufferedReader (new InputStreamReader (fs));
    
    // and now we read it in, just like in the code that runs on a single machine
    String cur = myReader.readLine (); 
    while (cur != null) {
      VectorizedObject temp = new VectorizedObject (cur);
      oldClusters.add (temp);
      VectorizedObject newCluster = temp.copy ();
      newCluster.setValue ("0");
      newClusters.add (newCluster);
      cur = myReader.readLine (); 
    }
  }
  
  public void map (LongWritable key, Text value, Context context) throws IOException, InterruptedException {
    
    // put your code here!
  }
  
  protected void cleanup (Context context) throws IOException, InterruptedException {
    
    // out your code here!
  }
}


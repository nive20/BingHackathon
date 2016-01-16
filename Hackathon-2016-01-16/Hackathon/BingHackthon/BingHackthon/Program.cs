using Accord.Controls;
using Accord.IO;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;
using System.Data;
using System.IO;
using System.Reflection;
using Accord.MachineLearning.Bayes;
using Accord.MachineLearning.VectorMachines.Learning;
using Accord.MachineLearning.VectorMachines;
using Accord.MachineLearning;

namespace BingHackthon
{
    class Program
    {
        static void Main(string[] args)
        {
            #region data prep
            string[] input1 = File.ReadAllLines("BingHackathonTestData.txt");
            DataTable table = new DataTable();


            table.Columns.Add("RecordID", typeof(string));
            table.Columns.Add("Topic", typeof(string));
            table.Columns.Add("PUblicationYear", typeof(string));
            table.Columns.Add("Authors", typeof(string));
            table.Columns.Add("Title", typeof(string));
            table.Columns.Add("Summary", typeof(string));


            foreach (string item in input1)
            {
                string[] inputrray = item.Replace(". ", "").Split('	');
                string[] s = new string[6];
                for (int i = 0; i < 6; i++)
                {
                    s[i] = inputrray[i];
                };
                table.Rows.Add(s);
            }

            //Console.WriteLine(table); 
            #endregion

            #region TO Csv
            var dt = table;
            StringBuilder sb = new StringBuilder();

            IEnumerable<string> columnNames = dt.Columns.Cast<DataColumn>().
                                              Select(column => column.ColumnName);
            sb.AppendLine(string.Join(",", columnNames));

            foreach (DataRow row in dt.Rows)
            {
                IEnumerable<string> fields = row.ItemArray.Select(field => field.ToString());
                sb.AppendLine(string.Join(",", fields));
            }

            File.WriteAllText("test.csv", sb.ToString());
            #endregion


            #region Bag Of words
            
            #endregion

        }
    }
}

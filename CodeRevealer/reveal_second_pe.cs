/*
* This program the decrypt the actual trojan which
* located in the resources of the first PE
*/

using System.Text;
using System.IO;

namespace Reveal_ObfuscatedVBScriptTrojan
{
    class Program
    {
        static void Main(string[] args)
        {
            byte[] buffer = File.ReadAllBytes("DMPaOOU");

            for (int i = 0; i < buffer.Length; i++)
            {
                buffer[i] = (byte)(buffer[i] ^ Encoding.Unicode.GetBytes("Y74zGHeXtV3AXXVqtbFIBg5")[i % 0x10]);
            }

            File.WriteAllBytes("second_PE.exe.dontrun", buffer);
        }
    }
}
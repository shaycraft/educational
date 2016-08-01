// see problem at http://www.geeksforgeeks.org/check-if-a-given-sequence-of-moves-for-a-robot-is-circular-or-not/

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace interview_circle
{
    public class Program
    {
        public static string[] doesCircleExists(string[] commands)
        {
            List<string> answers = new List<string>();
            foreach (var cmd in commands)
            {
                int prev_dir = getNewDirection(0, cmd);
                int prev_change = 4 - prev_dir;
                int curr_dir = getNewDirection(prev_dir, cmd);
#if DEBUG
                Console.WriteLine("DEBUG:  new direction = " + curr_dir);
#endif
                int change = Math.Abs(curr_dir - prev_dir);
                if (change == prev_change)
                {
                    answers.Add("YES");
                }
                else
                {
                    answers.Add("NO");
                }
            }

            return answers.ToArray();
        }

        public static int getNewDirection(int dir, string cmd)
        {
            // dir:  0 north, 1 west, 2 south and 3 east
            int curr_dir = dir;

            for (int i = 0; i < cmd.Length; i++)
            {
                switch (cmd[i])
                {
                    case 'G':
                        break;
                    case 'L':
                        curr_dir = (curr_dir + 1) % 4;
                        break;
                    case 'R':
                        curr_dir = (curr_dir - 1) % 4;
                        break;
                }
            }
            return curr_dir;
        }

        #region private methods

        private static string[] input_console()
        {
            int _command_size = Convert.ToInt32(Console.ReadLine());
            string[] _commands = new string[_command_size];
            for (int i = 0; i < _command_size; i++)
            {
                _commands[i] = Console.ReadLine();
            }

            return _commands;
        }

        private static string[] input_hardcode()
        {
            return new string[] { "GGRL", "LL", "LR" };
        }

        #endregion

        public static void Main(String[] args)
        {
            string[] res;

            string[] _commands;
            _commands = input_console();
            //_commands = input_hardcode();
            int _commands_size = _commands.Length;

            res = doesCircleExists(_commands);
            for (int res_i = 0; res_i < res.Length; res_i++)
            {
                Console.WriteLine("{0} : {1}", _commands[res_i], res[res_i]);
            }
        }
    }
}

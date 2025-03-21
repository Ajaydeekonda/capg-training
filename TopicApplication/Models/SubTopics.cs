using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using TopicApplication.Models;


namespace TopicApplication.Models
{
    public class SubTopics
    {
        [Key]
        public int SubTopicID { get; set; }

        [Required]
        public string SubTopic { get; set; }

        [Required]
        public int TopicID { get; set; }
        [ForeignKey("TopicID")]
        public Topics Topic { get; set; }
    }
}

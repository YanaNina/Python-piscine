languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

print("Python was created by {Python}\n"
      "Ruby was created by {Ruby}\n"
      "PHP was creted by {PHP}".format(**languages))
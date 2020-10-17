function onSubmit() {
  var reg_other = document.getElementById("reg_other");
  var reg_other_in = document.getElementById("reg_other_in").value;

  var job_other = document.getElementById("job_other");
  var job_other_in = document.getElementById("job_other_in").value;

  var type_other = document.getElementById("type_other");
  var type_other_in = document.getElementById("type_other_in").value;

  reg_other.value = reg_other_in;
  job_other.value = job_other_in;
  type_other.value = type_other_in;
}

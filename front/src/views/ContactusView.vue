<template>
  <div class="container">
    <div class="row-fluid">
    <p style="width:100px"></p>

    <h2 class="contact"> 오시는 길</h2>
    <p style="width:100px"></p>
      <div class="span8">
        <iframe width="100%" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3165.280114153881!2d127.03747101558709!3d37.50131103561796!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x357ca3ff67128961%3A0x55a56e8ffc5bc5d!2z66mA7Yuw7Lqg7Y287IqkIOyXreyCvA!5e0!3m2!1sko!2skr!4v1653450728913!5m2!1sko!2skr"></iframe>
      </div>
      <p></p>
      <div class="span4">

      </div>
    </div>
    <div class="row" id="contact">
      <div class="col-sm-12 col-md-6 col-lg-3 my-5">
      </div>
      <div class="col-sm-12 col-md-6 col-lg-3 my-5">
        <div class="card border-0">
          <div class="card-body text-center contact-i">
            <i class="contact-i fa fa-phone fa-5x mb-3" aria-hidden="true"></i>
            <h4 class="contact-i text-uppercase mb-5">call us</h4>
            <p class="contact-p">02-1234-5678</p>
            <p class="contact-p">010-1234-5678</p>
          </div>
        </div>
      </div>
      <div class="col-sm-12 col-md-6 col-lg-3 my-5">
        <div class="card border-0">
          <div class="card-body text-center contact-i">
            <i class=" contact-i fa fa-envelope fa-5x mb-3" aria-hidden="true"></i>
            <h4 class="contact-i text-uppercase mb-5">email us</h4>
            <a href="mailto:jakeone722@gmail.com" class="contact-p">jakeone722@gmail.com</a>
            <p></p>
            <a href="mailto:dytjd297@gmail.com" class="contact-p">dytjd297@gmail.com</a>
            <p></p>
          </div>
        </div>
      </div>
      <div class="col-sm-12 col-md-6 col-lg-3 my-5">
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name : 'ContactUs'
}

</script>

<style>
.contact-i {
  color: #FFCC5B
}

.contact-p {
  color: #7C683C;
  text-decoration: none;
}

.contact {
  font-family: 'Do Hyeon', sans-serif;
  font-weight: bolder;
  font-size: 3em;
  margin: 1em;
}
</style>
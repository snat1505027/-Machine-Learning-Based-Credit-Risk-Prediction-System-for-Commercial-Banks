/*
 * SmartWizard 3.3.1 plugin
 * jQuery Wizard control Plugin
 * by Dipu
 *
 * Refactored and extended:
 * https://github.com/mstratman/jQuery-Smart-Wizard
 *
 * Original URLs:
 * http://www.techlaboratory.net
 * http://tech-laboratory.blogspot.com
 */


function blobToFile(theBlob, fileName){
    //A Blob() is almost a File() - it's just missing the two properties below which we will add
    theBlob.lastModifiedDate = new Date();
    theBlob.name = fileName;
    return theBlob;
}

function SmartWizard(target, options) {
    this.target       = target;
    this.options      = options;
    this.curStepIdx   = options.selected;
    this.steps        = $(target).children("ul").children("li").children("a"); // Get all anchors
    //this.form         = $(target).children("form")
    this.contentWidth = 0;
    this.msgBox = $('<div class="msgBox"><div class="content"></div><a href="#" class="close">X</a></div>');
    this.elmStepContainer = $('<div></div>').addClass("stepContainer");
    this.loader = $('<div>Loading</div>').addClass("loader");
    this.buttons = {
        next : $('<a>'+options.labelNext+'</a>').attr("href","#").addClass("buttonNext"),
        previous : $('<a>'+options.labelPrevious+'</a>').attr("href","#").addClass("buttonPrevious"),
        finish  : $('<a>'+options.labelFinish+'</a>').attr("href","loan_app_success.html").addClass("buttonFinish")
    };

    /*
     * Private functions
     */

    var _init = function($this) {
        var elmActionBar = $('<div></div>').addClass("actionBar");
        elmActionBar.append($this.msgBox);
        $('.close',$this.msgBox).click(function() {
            $this.msgBox.fadeOut("normal");
            return false;
        });

        var allDivs = $this.target.children('div');
        $this.target.children('ul').addClass("anchor");
        allDivs.addClass("content");

        // highlight steps with errors
        if($this.options.errorSteps && $this.options.errorSteps.length>0){
            $.each($this.options.errorSteps, function(i, n){
                $this.setError({ stepnum: n, iserror:true });
            });
        }

        $this.elmStepContainer.append(allDivs);
        elmActionBar.append($this.loader);
        $this.target.append($this.elmStepContainer);
        elmActionBar.append($this.buttons.finish)
                    .append($this.buttons.next)
                    .append($this.buttons.previous);
        $this.target.append(elmActionBar);
        this.contentWidth = $this.elmStepContainer.width();

        $($this.buttons.next).click(function() {
            $this.goForward();
            return false;
        });
        $($this.buttons.previous).click(function() {
            $this.goBackward();
            return false;
        });
        $($this.buttons.finish).click(function() {
		window.alert('hello');
            if(!$(this).hasClass('buttonDisabled')){
                //=============================== Getting radio button values ===========================
                var ele = document.getElementsByName('grade');
                var grade = "";
                for(i = 0; i < ele.length; i++) { 
                    if(ele[i].checked) 
                    grade = ele[i].value; 
                }

                var ele3 = document.getElementsByName('home_ownership');
                var home_ownership = "";
                for(i = 0; i < ele3.length; i++) { 
                    if(ele3[i].checked) 
                    home_ownership = ele3[i].value; 
                }

                var ele4 = document.getElementsByName('hardship_flag');
                var hardship_flag = "";
                for(i = 0; i < ele4.length; i++) { 
                    if(ele4[i].checked) 
                    hardship_flag = ele4[i].value; 
                }

                var ele5 = document.getElementsByName('hardship_status');
                var hardship_status = "";
                for(i = 0; i < ele5.length; i++) { 
                    if(ele5[i].checked) 
                    hardship_status = ele5[i].value; 
                }

                var ele6 = document.getElementsByName('hardship_loan_status');
                var hardship_loan_status = "";
                for(i = 0; i < ele6.length; i++) { 
                    if(ele6[i].checked) 
                    hardship_loan_status = ele6[i].value; 
                }

                var ele7 = document.getElementsByName('debt_settlement_flag');
                var debt_settlement_flag = "";
                for(i = 0; i < ele7.length; i++) { 
                    if(ele7[i].checked) 
                    debt_settlement_flag = ele7[i].value; 
                }

                var ele8 = document.getElementsByName('settlement_status');
                var settlement_status = "";
                for(i = 0; i < ele8.length; i++) { 
                    if(ele8[i].checked) 
                    settlement_status = ele8[i].value; 
                }

                var ele9 = document.getElementsByName('disbursement_method');
                var disbursement_method = "";
                for(i = 0; i < ele9.length; i++) { 
                    if(ele9[i].checked) 
                    disbursement_method = ele9[i].value; 
                }

                //============================== Getting date values =============================

                var date = new Date($('#sec_app_earliest_cr_line').val());
                day = date.getDate();
                month = date.getMonth() + 1;
                year = date.getFullYear();
                var sec_app_earliest_cr_line=[day, month, year].join('/');

                date = new Date($('#hardship_start_date').val());
                day = date.getDate();
                month = date.getMonth() + 1;
                year = date.getFullYear();
                var hardship_start_date=[day, month, year].join('/');

                date = new Date($('#hardship_end_date').val());
                day = date.getDate();
                month = date.getMonth() + 1;
                year = date.getFullYear();
                var hardship_end_date=[day, month, year].join('/');

                date = new Date($('#payment_plan_start_date').val());
                day = date.getDate();
                month = date.getMonth() + 1;
                year = date.getFullYear();
                var payment_plan_start_date=[day, month, year].join('/');

                date = new Date($('#debt_settlement_flag_date').val());
                day = date.getDate();
                month = date.getMonth() + 1;
                year = date.getFullYear();
                var debt_settlement_flag_date=[day, month, year].join('/');

                date = new Date($('#settlement_date').val());
                day = date.getDate();
                month = date.getMonth() + 1;
                year = date.getFullYear();
                var settlement_date=[day, month, year].join('/');

                
                
                window.alert($("#loan_amount").val()+ " " + $("#term").val() + " " + $("#interest_rate").val() + " " +hardship_start_date+" "+ "radio buttons test");

                var fd = new FormData();
                //============= 1-10 left (verification, pymnt_plan) ====================
                fd.append('loan_amount', $("#loan_amount").val());
                fd.append('term', $("#term").val());
                fd.append('interest_rate', $("#interest_rate").val());
                fd.append('installment', $("#installment").val());
                fd.append('grade', grade);
                fd.append('home_ownership', home_ownership);
                fd.append('annual_income', $("#annual_income").val());
                fd.append('purpose', $("#purpose").val());
                //============ 11-20 (dti)========================
                fd.append('addr_state', $("#addr_state").val());
                fd.append('delinq_2yrs', $("#delinq_2yrs").val());
                fd.append('inq_last_6mths', $("#inq_last_6mths").val());
                fd.append('mths_since_last_delinq', $("#mths_since_last_delinq").val());
                fd.append('mths_since_last_record', $("#mths_since_last_record").val());
                fd.append('open_acc', $("#open_acc").val());
                fd.append('pub_rec', $("#pub_rec").val());
                fd.append('revol_bal', $("#revol_bal").val());
                fd.append('revol_util', $("#revol_util").val());
                //============ 21-30===============================
                fd.append('total_acc', $("#total_acc").val());
                fd.append('open_act_il', $("#open_act_il").val());
                fd.append('acc_open_past_24mths', $("#acc_open_past_24mths").val());
                fd.append('avg_cur_bal', $("#avg_cur_bal").val());
                fd.append('bc_open_to_buy', $("#bc_open_to_buy").val());
                fd.append('bc_util', $("#bc_util").val());
                fd.append('chargeoff_within_12_mths', $("#chargeoff_within_12_mths").val());
                fd.append('delinq_amnt', $("#delinq_amnt").val());
                fd.append('mo_sin_old_il_acct', $("#mo_sin_old_il_acct").val());
                fd.append('mo_sin_old_rev_tl_op', $("#mo_sin_old_rev_tl_op").val());
                //=========== 31-40 =================================
                fd.append('mo_sin_rcnt_rev_tl_op', $("#mo_sin_rcnt_rev_tl_op").val());
                fd.append('mo_sin_rcnt_tl', $("#mo_sin_rcnt_tl").val());
                fd.append('mort_acc', $("#mort_acc").val());
                fd.append('mths_since_recent_bc', $("#mths_since_recent_bc").val());
                fd.append('mths_since_recent_bc_dlq', $("#mths_since_recent_bc_dlq").val());
                fd.append('mths_since_recent_inq', $("#mths_since_recent_inq").val());
                fd.append('mths_since_recent_revol_delinq', $("#mths_since_recent_revol_delinq").val());
                fd.append('num_accts_ever_120_pd', $("#num_accts_ever_120_pd").val());
                fd.append('num_actv_bc_tl', $("#num_actv_bc_tl").val());
                fd.append('num_actv_rev_tl', $("#num_actv_rev_tl").val());
                //=========== 41-50 =================================
                fd.append('num_bc_sats', $("#num_bc_sats").val());
                fd.append('num_bc_tl', $("#num_bc_tl").val());
                fd.append('num_il_tl', $("#num_il_tl").val());
                fd.append('num_op_rev_tl', $("#num_op_rev_tl").val());
                fd.append('num_rev_accts', $("#num_rev_accts").val());
                fd.append('num_rev_tl_bal_gt_0', $("#num_rev_tl_bal_gt_0").val());
                fd.append('num_sats', $("#num_sats").val());
                fd.append('num_tl_120dpd_2m', $("#num_tl_120dpd_2m").val());
                fd.append('num_tl_30dpd', $("#num_tl_30dpd").val());
                fd.append('num_tl_90g_dpd_24m', $("#num_tl_90g_dpd_24m").val());
                //=========== 51-60 =================================
                fd.append('num_tl_op_past_12m', $("#num_tl_op_past_12m").val());
                fd.append('pct_tl_nvr_dlq', $("#pct_tl_nvr_dlq").val());
                fd.append('percent_bc_gt_75', $("#percent_bc_gt_75").val());
                fd.append('pub_rec_bankruptcies', $("#pub_rec_bankruptcies").val());
                fd.append('tax_liens', $("#tax_liens").val());
                fd.append('tot_hi_cred_lim', $("#tot_hi_cred_lim").val());
                fd.append('total_bal_ex_mort', $("#total_bal_ex_mort").val());
                fd.append('total_bc_limit', $("#total_bc_limit").val());
                fd.append('total_il_high_credit_limit', $("#total_il_high_credit_limit").val());
                fd.append('revol_bal_joint', $("#revol_bal_joint").val());
                //=========== 61-70 =================================
                fd.append('sec_app_earliest_cr_line', sec_app_earliest_cr_line);
                fd.append('sec_app_inq_last_6mths', $("#sec_app_inq_last_6mths").val());
                fd.append('sec_app_mort_acc', $("#sec_app_mort_acc").val());
                fd.append('sec_app_open_acc', $("#sec_app_open_acc").val());
                fd.append('sec_app_revol_util', $("#sec_app_revol_util").val());
                fd.append('sec_app_open_act_il', $("#sec_app_open_act_il").val());
                fd.append('sec_app_num_rev_accts', $("#sec_app_num_rev_accts").val());
                fd.append('sec_app_chargeoff_within_12_mths', $("#sec_app_chargeoff_within_12_mths").val());
                fd.append('sec_app_collections_12_mths_ex_med', $("#sec_app_collections_12_mths_ex_med").val());
                fd.append('sec_app_mths_since_last_major_derog', $("#sec_app_mths_since_last_major_derog").val());
                //=========== 71-80 =================================
                fd.append('hardship_flag', hardship_flag);
                fd.append('hardship_type', $("#hardship_type").val());
                fd.append('hardship_reason', $("#hardship_reason").val());
                fd.append('hardship_status', hardship_status);
                fd.append('deferral_term', $("#deferral_term").val());
                fd.append('hardship_amount', $("#hardship_amount").val());
                fd.append('hardship_start_date', $("#hardship_start_date").val());
                fd.append('hardship_end_date', $("#hardship_end_date").val());
                fd.append('payment_plan_start_date', $("#payment_plan_start_date").val());
                fd.append('hardship_length', $("#hardship_length").val());
                //=========== 81-90 =================================
                fd.append('hardship_dpd', $("#hardship_dpd").val());
                fd.append('hardship_loan_status', hardship_loan_status);
                fd.append('orig_projected_additional_accrued_interest', $("#orig_projected_additional_accrued_interest").val());
                fd.append('hardship_payoff_balance_amount', $("#hardship_payoff_balance_amount").val());
                fd.append('hardship_last_payment_amount', $("#hardship_last_payment_amount").val());
                fd.append('disbursement_method', disbursement_method);
                fd.append('debt_settlement_flag', debt_settlement_flag);
                fd.append('debt_settlement_flag_date', debt_settlement_flag_date);
                fd.append('settlement_status', settlement_status);
                fd.append('settlement_date', settlement_date);
                //=========== 91-93 =================================
                fd.append('settlement_amount', $("#settlement_amount").val());
                fd.append('settlement_percentage', $("#settlement_percentage").val());
                fd.append('settlement_term', $("#settlement_term").val());
                
                window.alert("DATA Reading done!!");
                
                $.ajax({
                    type: 'POST',
                    url: '/polls/handleForm/',
                    data: fd,
                    processData: false,
                    contentType: false
                }).done(function(data) {
                       console.log(data);
                });

                
                if($.isFunction($this.options.onFinish)) {

                    var context = { fromStep: $this.curStepIdx + 1 };
                    if(!$this.options.onFinish.call(this,$($this.steps), context)){
                        return false;
                    }
                }else{

                    if(frm && frm.length){

                        // COME HERE , FORM SUBMIT, CODE HERE
                        
                        frm.submit();
                    }
                }
            }
            return false;

        });

        $($this.steps).bind("click", function(e){
            if($this.steps.index(this) == $this.curStepIdx){
                return false;
            }
            var nextStepIdx = $this.steps.index(this);
            var isDone = $this.steps.eq(nextStepIdx).attr("isDone") - 0;
            if(isDone == 1){
                _loadContent($this, nextStepIdx);
            }
            return false;
        });

        // Enable keyboard navigation
        if($this.options.keyNavigation){
            $(document).keyup(function(e){
                if(e.which==39){ // Right Arrow
                    $this.goForward();
                }else if(e.which==37){ // Left Arrow
                    $this.goBackward();
                }
            });
        }
        //  Prepare the steps
        _prepareSteps($this);
        // Show the first slected step
        _loadContent($this, $this.curStepIdx);
    };

    var _prepareSteps = function($this) {
        if(! $this.options.enableAllSteps){
            $($this.steps, $this.target).removeClass("selected").removeClass("done").addClass("disabled");
            $($this.steps, $this.target).attr("isDone",0);
        }else{
            $($this.steps, $this.target).removeClass("selected").removeClass("disabled").addClass("done");
            $($this.steps, $this.target).attr("isDone",1);
        }

        $($this.steps, $this.target).each(function(i){
            $($(this).attr("href").replace(/^.+#/, '#'), $this.target).hide();
            $(this).attr("rel",i+1);
        });
    };

    var _step = function ($this, selStep) {
        return $(
            $(selStep, $this.target).attr("href").replace(/^.+#/, '#'),
            $this.target
        );
    };

    var _loadContent = function($this, stepIdx) {
        var selStep = $this.steps.eq(stepIdx);
        var ajaxurl = $this.options.contentURL;
        var ajaxurl_data = $this.options.contentURLData;
        var hasContent = selStep.data('hasContent');
        var stepNum = stepIdx+1;
        if (ajaxurl && ajaxurl.length>0) {
            if ($this.options.contentCache && hasContent) {
                _showStep($this, stepIdx);
            } else {
                var ajax_args = {
                    url: ajaxurl,
                    type: "POST",
                    data: ({step_number : stepNum}),
                    dataType: "text",
                    beforeSend: function(){
                        $this.loader.show();
                    },
                    error: function(){
                        $this.loader.hide();
                    },
                    success: function(res){
                        $this.loader.hide();
                        if(res && res.length>0){
                            selStep.data('hasContent',true);
                            _step($this, selStep).html(res);
                            _showStep($this, stepIdx);
                        }
                    }
                };
                if (ajaxurl_data) {
                    ajax_args = $.extend(ajax_args, ajaxurl_data(stepNum));
                }
                $.ajax(ajax_args);
            }
        }else{
            _showStep($this,stepIdx);
        }
    };

    var _showStep = function($this, stepIdx) {
        var selStep = $this.steps.eq(stepIdx);
        var curStep = $this.steps.eq($this.curStepIdx);
        if(stepIdx != $this.curStepIdx){
            if($.isFunction($this.options.onLeaveStep)) {
                var context = { fromStep: $this.curStepIdx+1, toStep: stepIdx+1 };
                if (! $this.options.onLeaveStep.call($this,$(curStep), context)){
                    return false;
                }
            }
        }

        $this.elmStepContainer.height(_step($this, selStep).outerHeight());
        var prevCurStepIdx = $this.curStepIdx;
        $this.curStepIdx =  stepIdx;
        if ($this.options.transitionEffect == 'slide'){
            _step($this, curStep).slideUp("fast",function(e){
                _step($this, selStep).slideDown("fast");
                _setupStep($this,curStep,selStep);
            });
        } else if ($this.options.transitionEffect == 'fade'){
            _step($this, curStep).fadeOut("fast",function(e){
                _step($this, selStep).fadeIn("fast");
                _setupStep($this,curStep,selStep);
            });
        } else if ($this.options.transitionEffect == 'slideleft'){
            var nextElmLeft = 0;
            var nextElmLeft1 = null;
            var nextElmLeft = null;
            var curElementLeft = 0;
            if(stepIdx > prevCurStepIdx){
                nextElmLeft1 = $this.contentWidth + 10;
                nextElmLeft2 = 0;
                curElementLeft = 0 - _step($this, curStep).outerWidth();
            } else {
                nextElmLeft1 = 0 - _step($this, selStep).outerWidth() + 20;
                nextElmLeft2 = 0;
                curElementLeft = 10 + _step($this, curStep).outerWidth();
            }
            if (stepIdx == prevCurStepIdx) {
                nextElmLeft1 = $($(selStep, $this.target).attr("href"), $this.target).outerWidth() + 20;
                nextElmLeft2 = 0;
                curElementLeft = 0 - $($(curStep, $this.target).attr("href"), $this.target).outerWidth();
            } else {
                $($(curStep, $this.target).attr("href"), $this.target).animate({left:curElementLeft},"fast",function(e){
                    $($(curStep, $this.target).attr("href"), $this.target).hide();
                });
            }

            _step($this, selStep).css("left",nextElmLeft1).show().animate({left:nextElmLeft2},"fast",function(e){
                _setupStep($this,curStep,selStep);
            });
        } else {
            _step($this, curStep).hide();
            _step($this, selStep).show();
            _setupStep($this,curStep,selStep);
        }
        return true;
    };

    var _setupStep = function($this, curStep, selStep) {
        $(curStep, $this.target).removeClass("selected");
        $(curStep, $this.target).addClass("done");

        $(selStep, $this.target).removeClass("disabled");
        $(selStep, $this.target).removeClass("done");
        $(selStep, $this.target).addClass("selected");

        $(selStep, $this.target).attr("isDone",1);

        _adjustButton($this);

        if($.isFunction($this.options.onShowStep)) {
            var context = { fromStep: parseInt($(curStep).attr('rel')), toStep: parseInt($(selStep).attr('rel')) };
            if(! $this.options.onShowStep.call(this,$(selStep),context)){
                return false;
            }
        }
        if ($this.options.noForwardJumping) {
            // +2 == +1 (for index to step num) +1 (for next step)
            for (var i = $this.curStepIdx + 2; i <= $this.steps.length; i++) {
                $this.disableStep(i);
            }
        }
    };

    var _adjustButton = function($this) {
        if (! $this.options.cycleSteps){
            if (0 >= $this.curStepIdx) {
                $($this.buttons.previous).addClass("buttonDisabled");
				if ($this.options.hideButtonsOnDisabled) {
                    $($this.buttons.previous).hide();
                }
            }else{
                $($this.buttons.previous).removeClass("buttonDisabled");
                if ($this.options.hideButtonsOnDisabled) {
                    $($this.buttons.previous).show();
                }
            }
            if (($this.steps.length-1) <= $this.curStepIdx){
                $($this.buttons.next).addClass("buttonDisabled");
                if ($this.options.hideButtonsOnDisabled) {
                    $($this.buttons.next).hide();
                }
            }else{
                $($this.buttons.next).removeClass("buttonDisabled");
                if ($this.options.hideButtonsOnDisabled) {
                    $($this.buttons.next).show();
                }
            }
        }
        // Finish Button
        if (! $this.steps.hasClass('disabled') || $this.options.enableFinishButton){
            $($this.buttons.finish).removeClass("buttonDisabled");
            if ($this.options.hideButtonsOnDisabled) {
                $($this.buttons.finish).show();
            }
        }else{
            $($this.buttons.finish).addClass("buttonDisabled");
            if ($this.options.hideButtonsOnDisabled) {
                $($this.buttons.finish).hide();
            }
        }
    };

    /*
     * Public methods
     */

    SmartWizard.prototype.goForward = function(){
        //var frm = $this.target.parents('form'); //$(target).children("ul")
        //window.alert(frm+' '+ frm.length);
        var nextStepIdx = this.curStepIdx + 1;
        if (this.steps.length <= nextStepIdx){
            if (! this.options.cycleSteps){
                return false;
            }
            nextStepIdx = 0;
        }
        _loadContent(this, nextStepIdx);
    };

    SmartWizard.prototype.goBackward = function(){
        var nextStepIdx = this.curStepIdx-1;
        if (0 > nextStepIdx){
            if (! this.options.cycleSteps){
                return false;
            }
            nextStepIdx = this.steps.length - 1;
        }
        _loadContent(this, nextStepIdx);
    };

    SmartWizard.prototype.goToStep = function(stepNum){
        var stepIdx = stepNum - 1;
        if (stepIdx >= 0 && stepIdx < this.steps.length) {
            _loadContent(this, stepIdx);
        }
    };
    SmartWizard.prototype.enableStep = function(stepNum) {
        var stepIdx = stepNum - 1;
        if (stepIdx == this.curStepIdx || stepIdx < 0 || stepIdx >= this.steps.length) {
            return false;
        }
        var step = this.steps.eq(stepIdx);
        $(step, this.target).attr("isDone",1);
        $(step, this.target).removeClass("disabled").removeClass("selected").addClass("done");
    }
    SmartWizard.prototype.disableStep = function(stepNum) {
        var stepIdx = stepNum - 1;
        if (stepIdx == this.curStepIdx || stepIdx < 0 || stepIdx >= this.steps.length) {
            return false;
        }
        var step = this.steps.eq(stepIdx);
        $(step, this.target).attr("isDone",0);
        $(step, this.target).removeClass("done").removeClass("selected").addClass("disabled");
    }
    SmartWizard.prototype.currentStep = function() {
        return this.curStepIdx + 1;
    }

    SmartWizard.prototype.showMessage = function (msg) {
        $('.content', this.msgBox).html(msg);
        this.msgBox.show();
    }
    SmartWizard.prototype.hideMessage = function () {
        this.msgBox.fadeOut("normal");
    }
    SmartWizard.prototype.showError = function(stepnum) {
        this.setError(stepnum, true);
    }
    SmartWizard.prototype.hideError = function(stepnum) {
        this.setError(stepnum, false);
    }
    SmartWizard.prototype.setError = function(stepnum,iserror) {
        if (typeof stepnum == "object") {
            iserror = stepnum.iserror;
            stepnum = stepnum.stepnum;
        }

        if (iserror){
            $(this.steps.eq(stepnum-1), this.target).addClass('error')
        }else{
            $(this.steps.eq(stepnum-1), this.target).removeClass("error");
        }
    }

    SmartWizard.prototype.fixHeight = function(){
        var height = 0;

        var selStep = this.steps.eq(this.curStepIdx);
        var stepContainer = _step(this, selStep);
        stepContainer.children().each(function() {
            height += $(this).outerHeight();
        });

        // These values (5 and 20) are experimentally chosen.
        stepContainer.height(height + 5);
        this.elmStepContainer.height(height + 20);
    }

    _init(this);
};



(function($){

$.fn.smartWizard = function(method) {
    var args = arguments;
    var rv = undefined;
    var allObjs = this.each(function() {
        var wiz = $(this).data('smartWizard');
        if (typeof method == 'object' || ! method || ! wiz) {
            var options = $.extend({}, $.fn.smartWizard.defaults, method || {});
            if (! wiz) {
                wiz = new SmartWizard($(this), options);
                $(this).data('smartWizard', wiz);
            }
        } else {
            if (typeof SmartWizard.prototype[method] == "function") {
                rv = SmartWizard.prototype[method].apply(wiz, Array.prototype.slice.call(args, 1));
                return rv;
            } else {
                $.error('Method ' + method + ' does not exist on jQuery.smartWizard');
            }
        }
    });
    if (rv === undefined) {
        return allObjs;
    } else {
        return rv;
    }
};

// Default Properties and Events
$.fn.smartWizard.defaults = {
    selected: 0,  // Selected Step, 0 = first step
    keyNavigation: true, // Enable/Disable key navigation(left and right keys are used if enabled)
    enableAllSteps: false,
    transitionEffect: 'fade', // Effect on navigation, none/fade/slide/slideleft
    contentURL:null, // content url, Enables Ajax content loading
    contentCache:true, // cache step contents, if false content is fetched always from ajax url
    cycleSteps: false, // cycle step navigation
    enableFinishButton: false, // make finish button enabled always
	hideButtonsOnDisabled: false, // when the previous/next/finish buttons are disabled, hide them instead?
    errorSteps:[],    // Array Steps with errors
    labelNext:'Next',
    labelPrevious:'Previous',
    labelFinish:'Finish',
    noForwardJumping: false,
    onLeaveStep: null, // triggers when leaving a step
    onShowStep: null,  // triggers when showing a step
    onFinish: null  // triggers when Finish button is clicked
};

})(jQuery);

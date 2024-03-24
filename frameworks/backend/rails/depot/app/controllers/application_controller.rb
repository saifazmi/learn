# frozen_string_literal: true

class ApplicationController < ActionController::Base
  before_action :set_global_variables

  private

  def set_global_variables
    @date_time_now = Time.now
  end
end

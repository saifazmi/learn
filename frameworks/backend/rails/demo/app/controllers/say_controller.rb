# frozen_string_literal: true

class SayController < ApplicationController
  def hello
    @time = Time.now
  end

  def goodbye; end
end
